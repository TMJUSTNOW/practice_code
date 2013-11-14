bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")


def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))


def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

# Implement pipeline_each so that the pipeline_each call
# above returns:


def pipeline_each(bands, rules):
    def rules_func(band, rules):
        if len(rules) == 0:
            return band
        return rules_func(rules[0](band), rules[1:])

    return map(lambda x: rules_func(x, rules), bands)


print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names])

# => [{'name': 'Sunset Rubdown', 'active': False, 'country': 'Canada'},
#     {'name': 'Women', 'active': False, 'country': 'Canada' },
#     {'name': 'A Silver Mt Zion', 'active': True, 'country': 'Canada'}]
