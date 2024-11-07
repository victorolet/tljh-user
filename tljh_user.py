from tljh.hooks import hookimpl

@hookimpl
def tljh_new_user_create(username):
    with open("test_new_user_create", "w") as f:
        f.write("file_written_by_simplest_plugin")
        f.write(username)