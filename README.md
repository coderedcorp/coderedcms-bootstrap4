Bootstrap 4 Theme for Wagtail CRX
=================================

This is a compatibility package for older sites built with `coderedcms` 0.x
series wishing to upgrade to 1.x series (which switched to Bootstrap 5) without
needing to make any frontend changes.

* Provides the older Bootstrap 4 templates from `coderedcms` version 0.25.
* Provides the older Sass/CSS files from `coderedcms` version 0.25.
* Provides Bootstrap 4.6.2 Sass and CSS/JS distribution.

Installation
------------

```
pip install coderedcms-bootstrap4
```

Then in your Django settings file, add `coderedcms_bootstrap4` **above**
`coderedcms` in `INSTALLED_APPS`. This will make this theme's templates and
static files override those shipped with `coderedcms`. Also add `bootstrap4`.

```python
INSTALLED_APPS = [
    ...
    "coderedcms_bootstrap4",
    "coderedcms",
    "bootstrap4",
    ...
]
```

That's it! Continue to extend templates or import static files as usual from
`coderedcms` and you will instead be getting the Bootstrap 4 versions from this
theme.

NOTE: This theme will be maintained with necessary bug fixes, but will not
receive any new designs or new features. It is recommended to eventually upgrade
your sites to Bootstrap 5.
