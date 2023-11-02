def loader(notebook_file,html):
    with open(notebook_file, "rt", encoding="utf-8") as fh:
        nb = nbformat.read(notebook_file, as_version=4)

    ep = nbconvert.preprocessors.ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb)

    html, resources = nbconvert.HTMLExporter().from_notebook_node(nb)

    return flask.Response(html, status=200, mimetype="text/html")

loader('/home/cas/Desktop/apocrypha/university/second_year/PYU22T10/poster_project/pycno.ipynb','pycno_update.html')