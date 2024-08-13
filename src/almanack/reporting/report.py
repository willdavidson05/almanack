"""
This module creates entropy reports
"""

from typing import Any, Dict

from tabulate import tabulate


def repo_report(data: Dict[str, Any]) -> str:
    """
    Returns the formatted entropy report as a string.

    Args:
        data (Dict[str, Any]): Dictionary with the entropy data.

    Returns:
        str: Formatted entropy report.
    """
    title = "Software Information Entropy Report"

    # Extract details from data
    repo_path = data["repo_path"]
    total_normalized_entropy = data["total_normalized_entropy"]
    number_of_commits = data["number_of_commits"]
    number_of_files = data["number_of_files"]
    time_range_of_commits = data["time_range_of_commits"]
    entropy_data = data["file_level_entropy"]

    # Sort files by normalized entropy in descending order and get the top 5
    sorted_entropy = sorted(
        entropy_data.items(), key=lambda item: item[1], reverse=True
    )
    top_files = sorted_entropy[:5]

    # Format the report
    repo_info = [
        ["Repository Path", repo_path],
        ["Total Normalized Entropy", f"{total_normalized_entropy:.4f}"],
        ["Number of Commits Analyzed", number_of_commits],
        ["Files Analyzed", number_of_files],
        [
            "Time Range of Commits",
            f"{time_range_of_commits[0]} to {time_range_of_commits[1]}",
        ],
    ]

    top_files_info = [
        [file_name, f"{normalized_entropy:.4f}"]
        for file_name, normalized_entropy in top_files
    ]

    report_content = f"""
{'=' * 80}
{title:^80}
{'=' * 80}

Repository information:
{tabulate(repo_info, tablefmt="simple_grid")}

Top 5 files with the most entropy:
{tabulate(top_files_info, headers=["File Name", "Normalized Entropy"], tablefmt="simple_grid")}

"""
    return report_content



def pr_report(data: Dict[str, Any]) -> str:
    """
    Returns the formatted PR-specific entropy report as a string.

    Args:
        data (Dict[str, Any]): Dictionary with the entropy data.

    Returns:
        str: Formatted GitHub markdown PR report.
    """
    title = "Pull Request Entropy Report"

    # Extract details from data
    pr_branch = data["pr_branch"]
    main_branch = data["main_branch"]
    total_entropy_introduced = data["total_entropy_introduced"]
    number_of_files_changed = data["number_of_files_changed"]
    entropy_data = data["entropy_per_file"]
    commits = data["commits"]

    # Sort files by normalized entropy in descending order and get the top 5
    sorted_entropy = sorted(entropy_data.items(), key=lambda item: item[1], reverse=True)
    top_files = sorted_entropy[:5]

    # Format the report
    pr_info = [
        ["PR Branch", pr_branch],
        ["Main Branch", main_branch],
        ["Total Entropy Introduced", f"{total_entropy_introduced:.4f}"],
        ["Number of Files Changed", number_of_files_changed],
        ["Commit Dates", f"{commits[0]} to {commits[1]}"],
    ]

    top_files_info = [
        [file_name, f"{entropy:.4f}"]
        for file_name, entropy in top_files
    ]

    report_content = f"""
{'=' * 80}
{title:^80}
{'=' * 80}

Pull Request Comparison:
{tabulate(pr_info, tablefmt="simple_grid")}

Top 5 Files with Highest Entropy:
{tabulate(top_files_info, headers=["File Name", "Entropy Introduced"], tablefmt="simple_grid")}

"""
    return report_content
