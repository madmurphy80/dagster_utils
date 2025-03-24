from models.db_resource import DbResource


class WpResource(DbResource):

    list_query = """
        SELECT ID AS id, post_name AS name, post_modified AS modified
        FROM wp_posts
        WHERE post_type = 'post' AND post_status = 'publish'
    """

    get_query = """
        SELECT ID AS source_id, 'wp' AS type, post_date AS created, post_modified AS modified, 'premium' AS access, post_name AS name, post_content AS content
        FROM wp_posts
        WHERE ID = :id
    """