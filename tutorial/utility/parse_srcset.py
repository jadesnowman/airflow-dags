def parse_srcset(srcset_raw):
    """
    Parses the `srcset` attribute into a list of dictionaries with URL and descriptor.
    
    Args:
        srcset_raw (str): The raw `srcset` string from the HTML.
    
    Returns:
        list: A list of dictionaries, each containing `url` and `descriptor`.
    """
    if not srcset_raw:
        return []
    
    return [
        {"url": item.split()[0], "descriptor": item.split()[1] if len(item.split()) > 1 else None}
        for item in srcset_raw.split(",")
    ]