#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# mpenny, 2021-Aug-28, Updated code to address todo's and pseudocode - now has CD() class that uses constructor, setters, getters, and a string method
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt' # our standard file used to write/read to and from
lstOfCDObjects = [] #global list value that is used throughout the script

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        ___str__: returns formatted string of objects.
        strCheck: static method that checks for empty values in the artist/title fields since these are not caught by a try function preceding
        this class call. 
    """

#constructor for the class
    def __init__(self,cd_id,cd_title,cd_artist):
        #attributes for constructor
        
        cd_title = CD.strCheck(cd_title)
        cd_artist = CD.strCheck(cd_artist)
        self.__id = cd_id
        self.__title = cd_title
        self.__artist = cd_artist
  
    #defining getter properties
    
    @property
    def cd_id(self):
        return self.__id
    
    @property
    def cd_title(self):
        return self.__title
    @property
    def cd_artist(self):
        return self.__artist
    
    #defining setter properties
    
    @cd_id.setter
    def cd_id(self, value):
        self.__id = value
    
    @cd_title.setter
    def cd_title(self, value):
        self.__title = value
        
    @cd_artist.setter
    def cd_artist(self,value):
        self.__artist = value
    
    def __str__(self):
        return str(self.cd_id) + ',' + self.cd_title + ',' + self.__artist
   
    @staticmethod
    def strCheck(stField):
        if(stField) == '':
            raise Exception('Input cannot be blank')
        else:
            return stField
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        read_file(file_name, CDlst): -> None
        write_file(file_name, CDlst): -> None
        
    """
    @staticmethod
    def read_file(file_name, CDlst):
        """Function to manage data ingestion from file to a list

        Reads the data from file identified by file_name into a list

        Args:
            file_name (string): name of file used to read the data from
            CDlst: list of CD entries that holds the CD inventory

        Returns:
            None.
        """
        CDlst.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                line = line.strip()
                CDlst.append(line)
            objFile.close()
        except FileNotFoundError as err:
            print('Error opening file. Make sure it exists.')
            print(err)
        
    
    @staticmethod
    def write_file(file_name, CDlst):
        """Writes a list object to a text file contains error handling in case the file doesn't load
    
            Args:
                file_name (string): name of file used to write the data to
                CDlst: list of CD entries that holds the CD inventory
    
            Returns:
                None.
            """
        try:
             objFile = open(strFileName, 'w')
             for row in CDlst:
                 objFile.write(str(row)+ '\n')
             objFile.close()
        except Exception as err:
            print('Error when trying to write to file: ')
            print(err)

# -- PRESENTATION (Input/Output) -- #
class IO:

     """Handling Input / Output, displays a menu in print_menu staticmethod
     and menu_choice takes user selection and returns it"""

     @staticmethod
     def print_menu():
        """Displays a menu of choices to the user in the below print statements.

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

     @staticmethod
     def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

     @staticmethod
     def show_inventory(CDlst):
        """Displays current inventory table


        Args:
            CDlst: a list that holds the CD data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID,CD,Artist')
        try:
            for row in CDlst:
                print(row)
            print('\n')
            print('======================================')
            print('\n')
        except Exception as e:
            print('Error reading data from table. Please check data fidelity')
            print(e)

     @staticmethod
     def add_CD():
        """Used to interactively gather data from a user by presenting prompts and cleaning up data entered
        before it is appended to a list. Uses CD class to make instance of the class, and return a formatted string that is 
        appended.


        Args:
            None.

        Returns:
            none

        """
        try:
            strID = int(input('Enter ID: ').strip())
            strTitle = input('What is the CD\'s title? ').strip()
            stArtist = input('What is the Artist\'s name? ').strip()
            usrCD = CD(strID,strTitle,stArtist)
            print('Data added: ' + usrCD.__str__())
        except ValueError as err:
           print('Invalid value entered. Please re-enter a number, title, and artist')
           print(err)
        lstOfCDObjects.append(usrCD)

# -- Main Body of Script -- #

while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        print('Terminating program...')
        break
    # 3.2 process load inventory, before displaying it
    elif strChoice == 'l':
        FileIO.read_file(strFileName, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist, add to list
        usrInput = IO.add_CD()
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 save to a file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(strFileName, lstOfCDObjects)
            print('Data written to file!')
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')