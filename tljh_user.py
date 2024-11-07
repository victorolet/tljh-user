from tljh.hooks import hookimpl

@hookimpl
def tljh_post_install():
    with open("test_tljh_post_install", "w") as f:
        f.write("file_written_by_simplest_plugin")

@hookimpl
def tljh_new_user_create(username):
    with open("test_new_user_create", "w") as f:
        f.write("file_written_by_simplest_plugin")
        f.write(username)
