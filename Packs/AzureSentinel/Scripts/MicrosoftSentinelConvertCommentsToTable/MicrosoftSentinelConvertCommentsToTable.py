import demistomock as demisto
from CommonServerPython import *
from itertools import chain
import ast


def format_comment(comment: dict) -> dict:
    """
    Converts a comment to a dictionary with the relevant fields.
    """
    return {
        'name': comment.get('name'),
        'message': comment.get('properties', {}).get('message'),
        'createdTimeUtc': comment.get('properties', {}).get('createdTimeUtc'),
        'userPrincipalName': comment.get('properties', {}).get('author', {}).get('userPrincipalName')
    }


def convert_to_table(context_results: str) -> CommandResults:
    """
    Args:
        context_results (str): String representing a list of dicts

    Returns:
        CommandResults: CommandResults object containing only readable_output
    """
    context_results = ast.literal_eval(context_results)

    context_formatted = [
        format_comment(comment) for comment in context_results
    ]

    md = tableToMarkdown(
        '',
        context_formatted,
        headers=[*dict.fromkeys(chain.from_iterable(context_formatted))],
        removeNull=True,
        sort_headers=False,
        headerTransform=pascalToSpace
    )

    return CommandResults(
        readable_output=md
    )


def main():
    context = dict_safe_get(
        demisto.callingContext,
        ['context', 'Incidents', 0, 'CustomFields', 'microsoftsentinelcomments'],
        {}
    )

    if not context:
        return_error('No data to present')

    return_results(convert_to_table(context))


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
