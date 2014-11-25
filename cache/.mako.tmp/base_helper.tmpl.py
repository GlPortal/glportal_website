# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1416950565.204662
_enable_loop = True
_template_filename = u'themes/glportal/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        if title and not post.meta('splitslider'):
            __M_writer(u'        <script type="text/javascript" src="/assets/js/jquery.ba-cond.min.js"></script>\n        <script type="text/javascript" src="/assets/js/jquery.splitslider.js"></script>\n        <script type="text/javascript" src="/assets/js/slider.js"></script>\n')
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        striphtml = _import_ns.get('striphtml', context.get('striphtml', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer(u"prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer(u'og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer(u'article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            __M_writer(u"'")
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>')
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        if permalink:
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(unicode(text))
                __M_writer(u'<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                __M_writer(u'            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n   <link rel="stylesheet" type="text/css" href="css/glportal.css" />\n')
        if title and not post.meta('splitslider'):
            __M_writer(u'        <link rel="stylesheet" type="text/css" href="css/slider.css" />\n        <link rel="stylesheet" type="text/css" href="css/slider-custom.css" />\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">\n')
            else:
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(_link("index", None, langname)))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 3, "25": 0, "32": 2, "33": 3, "34": 66, "35": 98, "36": 133, "37": 156, "38": 170, "39": 178, "45": 68, "58": 68, "59": 69, "60": 70, "61": 71, "62": 74, "63": 75, "64": 77, "65": 78, "66": 79, "67": 81, "68": 82, "69": 87, "70": 89, "71": 90, "72": 90, "73": 90, "74": 92, "75": 93, "76": 97, "77": 97, "78": 97, "84": 4, "113": 4, "114": 8, "115": 9, "116": 10, "117": 11, "118": 13, "119": 14, "120": 16, "121": 17, "122": 19, "123": 22, "124": 23, "125": 26, "126": 26, "127": 26, "128": 29, "129": 30, "130": 30, "131": 30, "132": 32, "133": 33, "134": 33, "135": 33, "136": 33, "137": 35, "138": 35, "139": 36, "140": 36, "141": 37, "142": 38, "143": 38, "144": 38, "145": 40, "146": 41, "147": 42, "148": 43, "149": 43, "150": 43, "151": 43, "152": 43, "153": 43, "154": 43, "155": 46, "156": 47, "157": 48, "158": 48, "159": 48, "160": 50, "161": 51, "162": 52, "163": 52, "164": 52, "165": 54, "166": 55, "167": 55, "168": 55, "169": 57, "170": 58, "171": 58, "172": 59, "173": 60, "174": 61, "175": 62, "176": 62, "177": 62, "178": 64, "179": 65, "180": 65, "186": 135, "198": 135, "199": 136, "200": 137, "201": 138, "202": 138, "203": 138, "204": 140, "205": 141, "206": 142, "207": 142, "208": 142, "209": 142, "210": 142, "211": 143, "212": 144, "213": 144, "214": 144, "215": 144, "216": 144, "217": 147, "218": 148, "219": 149, "220": 150, "221": 150, "222": 150, "223": 150, "224": 150, "225": 151, "226": 152, "227": 152, "228": 152, "229": 152, "230": 152, "236": 101, "249": 101, "250": 103, "251": 104, "252": 107, "253": 108, "254": 109, "255": 111, "256": 112, "257": 114, "258": 115, "259": 116, "260": 117, "261": 118, "262": 120, "263": 124, "264": 125, "265": 128, "266": 129, "267": 129, "268": 129, "269": 130, "270": 131, "271": 131, "272": 131, "278": 172, "288": 172, "289": 173, "290": 174, "291": 175, "292": 175, "293": 175, "294": 175, "295": 175, "296": 175, "297": 175, "303": 158, "314": 158, "315": 159, "316": 160, "317": 160, "318": 160, "319": 161, "320": 162, "321": 163, "322": 164, "323": 164, "324": 164, "325": 164, "326": 164, "327": 166, "328": 167, "329": 167, "330": 167, "336": 330}, "uri": "base_helper.tmpl", "filename": "themes/glportal/templates/base_helper.tmpl"}
__M_END_METADATA
"""
