from configparser import ConfigParser


def read_db_config(filename='SQL_Connector\\ConnectionConfig.ini', section='mysql'):

    # Initialize parser and read the file
    parser = ConfigParser()
    parser.read(filename)

    # Begin at the specified section
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} section is not present in the {1} file'.format(section, filename))

    return db

read_db_config()