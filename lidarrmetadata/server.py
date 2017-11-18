import cherrypy

from api import app
import models


def main():
    """
    Entry point for script
    """

    cherrypy.tree.graft(app, '/')
    cherrypy.config.update({
        'log.screen': True,
        'server.socket_port': 5000
    })

    models.database.connect()
    models.database.create_tables([models.Artist,
                                   models.Album,
                                   models.Track,
                                   models.Image],
                                  safe=True)
    models.database.close()

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()