if __name__ == '__main__':
    import sys
    approved_commands = ['run_migration', 'import_data']

    # if len(sys.argv) == 1:
    #     print 'enter some input'

    user_ip = sys.argv[1]

    if user_ip == 'run_migration':
        from migrations.DbMigrate import CreateTables
        db = CreateTables('zdata')
        db.migrate()


    if user_ip == 'import_data':
        print 'importing data'
        from csvimport.CsvImporter import DataImporter
        csvimporter = DataImporter()
        csvimporter.import_region_rent()

    if user_ip not in approved_commands:
        print 'command not recognized'
