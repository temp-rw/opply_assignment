from base.constants.enums import BaseEnum


class OrderStatuses(BaseEnum):
    RESERVED = 'reserved'  # order is paid and reserved for current customer
    IN_DELIVERY = 'in_delivery'  # order is on the way to customer
    DELIVERED = 'delivered'  # order is delivered
