import blog_app as bapp


if(__name__ == "__main__"):
    bapp = bapp.create_app()
    bapp.run(debug=True)