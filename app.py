from app_presentation import init_app


app = init_app()
if __name__ == '__main__':
    app.logger.debug('Starting application')
    app.run()
