if __name__ == '__main__':
    import sys
    from migrations.DbMigrate import CreateTables
    import connection
    import models

    approved_commands = ['run_migration', 'import_data']
    user_ip = sys.argv[1]

    if user_ip == 'run_migration':
        db = CreateTables('zdata')
        db.migrate()


    if user_ip == 'import_data':
        print 'importing data'

    if user_ip not in approved_commands:
        print 'command not recognized'
