import work_with_people as wwp
import work_with_file as wwf


def work_with_notebook():
    type = wwp.informatio_request()
    if type == 0:
        textLine = wwp.getUserInput()
        wwf.write_text(textLine)
        some_notb = wwf.read_text()
        wwf.print_notebook(some_notb)
    else:
        data_surname = wwp.import_text()
        some_notbook = wwf.read_text()
        wwf.search_tex(data_surname, some_notbook)
