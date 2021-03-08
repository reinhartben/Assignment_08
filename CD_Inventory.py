#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# BReinhart, 2021-Mar-07, added properties and constructor for CD class
# BReinhart, 2021-Mar-07, added doc strings, main body script, and FileIO class info
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__(): -> formatted string of CD data

    """

    # -- Constructor -- #
    def __init__(self, cdID, cdTitle, cdArtist):
        """Function to create a CD object
        
        Takes in CD info and saves in private attributes
        
        args:
            self: reference to particular CD object
            cdID (int): ID of CD
            cdTitle (string): Title of CD
            cdArtist (string): Artist of CD
        
        returns:
            None.
            
        """
        # -- Attributes -- #
        if not(str(cdID).isnumeric()):
            raise Exception('ID must be an integer!')
        else:
            self.__cd_id = cdID
        self.__cd_title = cdTitle
        self.__cd_artist = cdArtist

    # -- Properties -- #

    @property
    def cdID(self):
        """Getter function to return the specific ID of a CD
        
        args:
            self: reference to particular CD object
        
        returns:
            None
            
        """
        return self.__cd_id

    @cdID.setter
    def cdID(self, cdID):
        """Setter function to change the ID of a CD
        
        args:
            self: reference to particular CD object
            cdID (int): ID to change for the CD
        
        returns:
            None
            
        """
        if not(str(cdID).isnumeric()):
            raise Exception('ID must be an integer!')
        else:
            self.__cd_id = cdID

    @property
    def cdTitle(self):
        """Getter function to return the specific Title of a CD
        
        args:
            self: reference to particular CD object
        
        returns:
            None
            
        """
        return self.__cd_title

    @cdTitle.setter
    def cdTitle(self, cdTitle):
        """Setter function to change the Title of a CD
        
        args:
            self: reference to particular CD object
            Title (string): Title to change for the CD
        
        returns:
            None
            
        """
        if str(cdTitle).isnumeric():
            raise Exception('Title cannot be cryptic!')
        else:
            self.__cd_title = cdTitle

    @property
    def cdArtist(self):
        """Getter function to return the specific Artist of a CD
        
        args:
            self: reference to particular CD object
        
        returns:
            None
            
        """
        return self.__cd_artist

    @cdArtist.setter
    def cdArtist(self, cdArtist):
        """Setter function to change the Artist of a CD
        
        args:
            self: reference to particular CD object
            Artist (string): Artist to change for the CD
        
        returns:
            None
            
        """
        if str(cdArtist).isnumeric():
            raise Exception('Artist cannot be cryptic!')
        else:
            self.__cd_artist = cdArtist

    # -- Methods -- #

    def __str__(self):
        """Replacement string function to override standard obeject string function and format our CDs
        
        args:
            self: reference to particular CD object
        
        returns:
            Formatted string of CD data
            
        """
        return '{}\t{} (by: {})'.format(str(self.__cd_id), self.__cd_title, self.__cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    # -- Methods -- #

    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from text file to a list of CDs

        Reads the data from file identified by file_name into a 2D table
        (list of CDs) one line in the file represents one CD row in the table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            table: list of CDs generated from the file
            
        """
        table = []  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                cdRow = CD(int(data[0]), data[1], data[2])
                table.append(cdRow)
            objFile.close()
        except ValueError as e:
            print('ID entered is not an integer!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except FileNotFoundError as e:
            print('File does not exist! Data not loaded!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        return table

    @staticmethod
    def write_file(file_name, lst_Inventory):
        """Function to manage data saving from a list of dictionaries to a file

        Saves the data from a 2D table (list of dicts) identified by table.
        Each dictionary row in table is saved as a line to the file identified by file_name.
        
        Args:
            file_name (string): name of file used to save the data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
            
        """
        try:
            objFile = open(file_name, 'w')
            for row in lst_Inventory:
                lstValues = [str(row.cdID), row.cdTitle, row.cdArtist]
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except FileNotFoundError as e:
            print('File does not exist!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling input / output
    
    properties:
        None.
    
    methods:
        print_menu(): -> None
        menu_choice(): -> string of menu choice
        show_inventory(table): -> None
        cd_input(): -> list of strings of cd input
        
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
            
        """

        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            try:
                choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
            except Exception as e:
                print('There is a general error!')
                print('Built in error info:')
                print(type(e), e, e.__doc__, sep='\n')
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of CDs): 2D data structure (list of CDs) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def cd_input():
        """Gets user input for adding a CD to inventory
        
        Args:
            None.
        
        Returns:
            [strID (string), strTitle (string), strArtist (string)]: 
                a list of strings of the users input for the new CD ID, Title and Artist
                
        """
        try:
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
        except Exception as e:
            print('There is a general error!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        return [strID, strTitle, strArtist]

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # Let user exit program
    if strChoice == 'x':
        break
    # Let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        try:
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        except Exception as e:
            print('There is a general error!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            try:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            except Exception as e:
                print('There is a general error!')
                print('Built in error info:')
                print(type(e), e, e.__doc__, sep='\n')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # Let user add data to the inventory
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        addedCD = IO.cd_input()
        
        # Add item to the table
        while True:
            try:
                lstOfCDObjects.append(CD(addedCD[0], addedCD[1], addedCD[2]))
                break
            except Exception as e:
                print(e)
                addedCD[0] = input('Please re-enter the ID as an integer: ')

        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # Show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # Let user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        try:
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # Process choice
            if strYesNo == 'y':
                # save data
                FileIO.write_file(strFileName, lstOfCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        except Exception as e:
            print('There is a general error!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        continue  # start loop back at top.
    # Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

