import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import defaultdict

def fetch_github_data(endpoint, owner, repo, params=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}" if endpoint else f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = requests.get(url, params=params)
        if response.status_code == 403:
            return {'error': 'API rate limit exceeded'}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def fetch_repo_metadata(owner, repo):
    return fetch_github_data('', owner, repo)

def fetch_contributors(owner, repo):
    return fetch_github_data('contributors', owner, repo, {'per_page': 10})

def fetch_commits(owner, repo):
    return fetch_github_data('commits', owner, repo, {'per_page': 100})

def analyze_commit_activity(commits):
    activity = {
        'by_hour': defaultdict(int),
        'by_weekday': defaultdict(int),
        'by_month': defaultdict(int),  # still present for legacy use
        'by_year': defaultdict(int),
        'by_month_over_years': defaultdict(int),  # NEW: 'YYYY-MM' => count
        'by_day': defaultdict(int),
        'streaks': {'longest': 0, 'current': 0}
    }
    days_set = set()
    for commit in commits:
        if not isinstance(commit, dict):
            continue
        try:
            date = datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
            activity['by_hour'][date.hour] += 1
            activity['by_weekday'][date.strftime('%A')] += 1
            activity['by_month'][date.strftime('%B')] += 1  # legacy, not used for trends
            activity['by_year'][date.year] += 1
            month_over_years = date.strftime('%Y-%m')
            activity['by_month_over_years'][month_over_years] += 1
            day_str = date.strftime('%Y-%m-%d')
            activity['by_day'][day_str] += 1
            days_set.add(day_str)
        except (KeyError, ValueError):
            continue
    # Pad by_day so every day in the range is present
    if days_set:
        import calendar
        all_days = sorted(days_set)
        start_date = datetime.strptime(all_days[0], '%Y-%m-%d')
        end_date = datetime.strptime(all_days[-1], '%Y-%m-%d')
        # Pad by_day for every day of each month in the range
        pad_month = start_date.replace(day=1)
        end_month = end_date.replace(day=1)
        # Get today's date for truncation
        today = datetime(2025, 4, 21)
        while pad_month <= end_month:
            year = pad_month.year
            month = pad_month.month
            if year == today.year and month == today.month:
                last_day = today.day
            else:
                last_day = calendar.monthrange(year, month)[1]
            for day in range(1, last_day + 1):
                d = f"{year:04d}-{month:02d}-{day:02d}"
                if d not in activity['by_day'] and datetime(year, month, day) <= today:
                    activity['by_day'][d] = 0
            pad_month = pad_month + relativedelta(months=1)

        # Ensure all keys in by_day are strings and values are ints
        activity['by_day'] = {str(k): int(v) for k, v in activity['by_day'].items()}
        # Pad by_month_over_years for every month in the range
        month_set = set()
        month_counts = activity['by_month_over_years']
        curr_month = start_date.replace(day=1)
        last_month = end_date.replace(day=1)
        while curr_month <= last_month:
            key = curr_month.strftime('%Y-%m')
            if key not in month_counts:
                month_counts[key] = 0
            month_set.add(key)
            # Next month using relativedelta
            curr_month = curr_month + relativedelta(months=1)
        # Pad by_year for every year in the range
        year_counts = activity['by_year']
        for y in range(start_date.year, end_date.year+1):
            if str(y) not in year_counts:
                year_counts[str(y)] = 0
        # Ensure all keys in by_year are strings and values are ints
        activity['by_year'] = {str(k): int(v) for k, v in activity['by_year'].items()}
        # Calculate streaks (longest and current)
        sorted_days = sorted(days_set)
        longest = current = 1
        prev = sorted_days[0]
        for day in sorted_days[1:]:
            prev_date = datetime.strptime(prev, '%Y-%m-%d')
            curr_date = datetime.strptime(day, '%Y-%m-%d')
            if (curr_date - prev_date).days == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
            prev = day
        activity['streaks']['longest'] = longest
        activity['streaks']['current'] = current
    return activity