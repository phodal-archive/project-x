from peewee import *

database = MySQLDatabase('MK_xunzhao', **{'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class WpCommentmeta(BaseModel):
    comment = BigIntegerField(db_column='comment_id', index=True)
    meta = BigIntegerField(db_column='meta_id', primary_key=True)
    meta_key = CharField(index=True, null=True)
    meta_value = TextField(null=True)

    class Meta:
        db_table = 'wp_commentmeta'

class WpComments(BaseModel):
    comment = BigIntegerField(db_column='comment_ID', primary_key=True)
    comment_agent = CharField()
    comment_approved = CharField()
    comment_author = TextField()
    comment_author_ip = CharField(db_column='comment_author_IP')
    comment_author_email = CharField(index=True)
    comment_author_url = CharField()
    comment_content = TextField()
    comment_date = DateTimeField()
    comment_date_gmt = DateTimeField(index=True)
    comment_karma = IntegerField()
    comment_parent = BigIntegerField(index=True)
    comment_post = BigIntegerField(db_column='comment_post_ID', index=True)
    comment_type = CharField()
    user = BigIntegerField(db_column='user_id')

    class Meta:
        db_table = 'wp_comments'

class WpLinks(BaseModel):
    link_description = CharField()
    link = BigIntegerField(db_column='link_id', primary_key=True)
    link_image = CharField()
    link_name = CharField()
    link_notes = TextField()
    link_owner = BigIntegerField()
    link_rating = IntegerField()
    link_rel = CharField()
    link_rss = CharField()
    link_target = CharField()
    link_updated = DateTimeField()
    link_url = CharField()
    link_visible = CharField(index=True)

    class Meta:
        db_table = 'wp_links'

class WpOptions(BaseModel):
    autoload = CharField()
    option = BigIntegerField(db_column='option_id', primary_key=True)
    option_name = CharField(unique=True)
    option_value = TextField()

    class Meta:
        db_table = 'wp_options'

class WpPostmeta(BaseModel):
    meta = BigIntegerField(db_column='meta_id', primary_key=True)
    meta_key = CharField(index=True, null=True)
    meta_value = TextField(null=True)
    post = BigIntegerField(db_column='post_id', index=True)

    class Meta:
        db_table = 'wp_postmeta'

class WpPosts(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    comment_count = BigIntegerField()
    comment_status = CharField()
    guid = CharField()
    menu_order = IntegerField()
    ping_status = CharField()
    pinged = TextField()
    post_author = BigIntegerField(index=True)
    post_content = TextField(index=True)
    post_content_filtered = TextField()
    post_date = DateTimeField()
    post_date_gmt = DateTimeField()
    post_excerpt = TextField()
    post_mime_type = CharField()
    post_modified = DateTimeField()
    post_modified_gmt = DateTimeField()
    post_name = CharField(index=True)
    post_parent = BigIntegerField(index=True)
    post_password = CharField()
    post_status = CharField()
    post_title = TextField(index=True)
    post_type = CharField()
    to_ping = TextField()

    class Meta:
        db_table = 'wp_posts'

class WpPostviewsPlus(BaseModel):
    add_time = IntegerField()
    count = CharField(db_column='count_id', primary_key=True)
    gt = CharField()
    tv = CharField()

    class Meta:
        db_table = 'wp_postviews_plus'

class WpPrettyurls(BaseModel):
    disable_meta = IntegerField()
    meta_description = TextField(null=True)
    meta_keyword = TextField(null=True)
    meta_title = CharField(null=True)
    nofollow = IntegerField()
    target = CharField(db_column='target_id')
    target_type = CharField()
    url = CharField()

    class Meta:
        db_table = 'wp_prettyurls'

class WpSphCounter(BaseModel):
    counter = PrimaryKeyField(db_column='counter_id')
    max_doc = IntegerField(db_column='max_doc_id')

    class Meta:
        db_table = 'wp_sph_counter'

class WpSphStats(BaseModel):
    date_added = DateTimeField()
    keywords = CharField(index=True)
    keywords_full = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'wp_sph_stats'

class WpTermRelationships(BaseModel):
    object = BigIntegerField(db_column='object_id')
    term_order = IntegerField()
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id', index=True)

    class Meta:
        db_table = 'wp_term_relationships'
        primary_key = CompositeKey('object', 'term_taxonomy')

class WpTermTaxonomy(BaseModel):
    count = BigIntegerField()
    description = TextField()
    parent = BigIntegerField()
    taxonomy = CharField(index=True)
    term = BigIntegerField(db_column='term_id')
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id', primary_key=True)

    class Meta:
        db_table = 'wp_term_taxonomy'

class WpTerms(BaseModel):
    name = CharField(index=True)
    slug = CharField(index=True)
    term_group = BigIntegerField()
    term = BigIntegerField(db_column='term_id', primary_key=True)

    class Meta:
        db_table = 'wp_terms'

class WpUsermeta(BaseModel):
    meta_key = CharField(index=True, null=True)
    meta_value = TextField(null=True)
    umeta = BigIntegerField(db_column='umeta_id', primary_key=True)
    user = BigIntegerField(db_column='user_id', index=True)

    class Meta:
        db_table = 'wp_usermeta'

class WpUsers(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    display_name = CharField()
    user_activation_key = CharField()
    user_email = CharField()
    user_login = CharField(index=True)
    user_nicename = CharField(index=True)
    user_pass = CharField()
    user_registered = DateTimeField()
    user_status = IntegerField()
    user_url = CharField()

    class Meta:
        db_table = 'wp_users'

class WpYarppRelatedCache(BaseModel):
    id = BigIntegerField(db_column='ID', index=True)
    date = DateTimeField()
    reference = BigIntegerField(db_column='reference_ID')
    score = FloatField(index=True)

    class Meta:
        db_table = 'wp_yarpp_related_cache'
        primary_key = CompositeKey('id', 'reference')

