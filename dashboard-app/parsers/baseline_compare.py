def compare_lists(old, new):

    return {

        "added":
            list(set(new) - set(old)),

        "removed":
            list(set(old) - set(new))

    }
