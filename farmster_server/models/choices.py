from django.utils.translation import ugettext_lazy as _


class CROP_TYPE:
    def __init__(self):
        pass

    UNKNOWN = 'UNKNOWN'
    FRUIT = 'FRUIT'
    VEGETABLE = 'VEGETABLE'
    OTHER = 'OTHER'

    choices = (
        (UNKNOWN, _('UNKNOWN')),
        (FRUIT, _('FRUIT')),
        (VEGETABLE, _('VEGETABLE')),
        (OTHER, _('OTHER'))
    )


class AMOUNT_UNIT:
    def __init__(self):
        pass

    KGS = 'KGS'
    TONS = 'TONS'
    BOXES = 'BOXES'
    TRUCKS = 'TRUCKS'
    PIECES = 'PIECES'
    BAGS = 'BAGS'
    CRATES = 'CRATES'
    L = 'L'
    SACKS = 'SACKS'
    BUNDLES = 'BUNDLES'
    TREES = 'TREES'
    TINS = 'TINS'
    OTHER = 'OTHER'

    choices = (
        (KGS, _('KGS')),
        (TONS, _('TONS')),
        (BOXES, _('BOXES')),
        (TRUCKS, _('TRUCKS')),
        (PIECES, _('PIECES')),
        (BAGS, _('BAGS')),
        (CRATES, _('CRATES')),
        (L, _('L')),
        (SACKS, _('SACKS')),
        (BUNDLES, _('BUNDLES')),
        (TREES, _('TREES')),
        (TINS, _('TINS')),
        (OTHER, _('OTHER'))
    )


class CROP_LISTING_STATUS:
    def __init__(self):
        pass

    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'
    SOLD = 'SOLD'
    CANCELLED = 'CANCELLED'

    choices = (
        (ACTIVE, _('ACTIVE')),
        (EXPIRED, _('EXPIRED')),
        (SOLD, _('SOLD')),
        (CANCELLED, _('CANCELLED')),
    )


class PLACE_TYPE:
    def __init__(self):
        pass

    UNKNOWN = 'UNKNOWN'
    GROUP = 'GROUP'
    VILLAGE = 'VILLAGE'
    TOWN = 'TOWN'
    CITY = 'CITY'
    OTHER = 'OTHER'

    choices = (
        (UNKNOWN, _('UNKNOWN')),
        (GROUP, _('GROUP')),
        (VILLAGE, _('VILLAGE')),
        (TOWN, _('TOWN')),
        (CITY, _('CITY')),
        (OTHER, _('OTHER'))
    )


class SHIPPING_METHOD:
    def __init__(self):
        pass

    PICKUP = 'PICKUP'
    DELIVERY = 'DELIVERY'

    choices = (
        (PICKUP, _('PICKUP')),
        (DELIVERY, _('DELIVERY')),
    )


class PRICING_TYPE:
    def __init__(self):
        pass

    TOTAL = 'TOTAL'
    PER_KG = 'PER_KG'

    choices = (
        (TOTAL, _('TOTAL')),
        (PER_KG, _('PER_KG')),
    )


class CROP_QUALITY:
    def __init__(self):
        pass

    UNKNOWN = 'UNKNOWN'
    POOR = 'POOR'
    GOOD = 'GOOD'
    EXCELLENT = 'EXCELLENT'

    choices = (
        (UNKNOWN, _('UNKNOWN')),
        (POOR, _('POOR')),
        (GOOD, _('GOOD')),
        (EXCELLENT, _('EXCELLENT')),
    )


class CROP_SIZE:
    def __init__(self):
        pass

    UNKNOWN = 'UNKNOWN'
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'

    choices = (
        (UNKNOWN, _('UNKNOWN')),
        (SMALL, _('SMALL')),
        (MEDIUM, _('MEDIUM')),
        (LARGE, _('LARGE')),
    )