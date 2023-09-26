from utilities.choices import ChoiceSet


class NodeStatusChoices(ChoiceSet):
    STATUS_ACTIVE = 'active'
    STATUS_RESERVED = 'reserved'
    STATUS_DEPRECATED = 'deprecated'
    STATUS_UNCHECKED = 'unchecked'

    CHOICES = (
        (STATUS_ACTIVE, 'Active', 'blue'),
        (STATUS_RESERVED, 'Reserved', 'cyan'),
        (STATUS_DEPRECATED, 'Deprecated', 'red'),
        (STATUS_UNCHECKED, 'Unchecked', 'black'),
    )

class PoolAllowChoices(ChoiceSet):
    CHOICE_YES = 'yes'
    CHOICE_NO = 'no'

    CHOICES = (
        (CHOICE_YES, 'Yes', 'blue'),
        (CHOICE_NO, 'No', 'red'),
    )


class IPAddressFamilyChoices(ChoiceSet):

    FAMILY_4 = 'ipv4'
    FAMILY_6 = 'ipv6'

    CHOICES = (
        (FAMILY_4, 'IPv4'),
        (FAMILY_6, 'IPv6'),
    )