from django.utils.text import slugify


def slug_generator(instance, new_slug=None):
    if new_slug:
        slug = new_slug
    else:
        slug = f"{slugify(instance.title)}--{instance.pk}"
    return slug
