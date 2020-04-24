import os
import os, webbrowser, ctypes
import subprocess
import sys
import time
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call

#global variables
osval = 0
np = 2
dirpath = ""
gfile = ""
gfile2 = ""
gfile3 = ""
gfile4 = ""
dirpath = ""
temp_R = ""
rpath = ""
dirrpath = ""
rcommandsfile = ""

#Main MOTHUR GUI Menu
def mainmenu():
    #Define a function for a Button Widget button_quit.
    def popup():
        answer = messagebox.askquestion(" ","Do you want to exit the MOTHUR GUI Application ?")
        if answer == "yes":
            root.destroy()#End MOTHUR GUI
            
    root = tkinter.Tk()
    root.title ("MOTHUR GUI")
    root.geometry("300x400")

    #Define a Greeting message
    Hello_Msg = tkinter.Label(root, text = "\nWelcome To the MOTHUR GUI\n", font=("AR BLANCA", 15), fg='darkslategrey').pack(anchor=CENTER)
    Hello_Msg2 = tkinter.Label(root, text = "Please select from the following options\n", font=("AR BLANCA", 10), fg='darkslategrey').pack(anchor=CENTER)


    #---------------------This is the section for the main widget
    # Create a widget button to run MOTHUR
    b = Button(root, text = 'Run MOTHUR', bg='SlateGray2', fg='midnight blue', command = runmothurinstr, width = 20).pack(anchor=CENTER)
    space1_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    # Create a widget button to run R
    b1 = Button(root, text = 'Run R',bg='SlateGray2', fg='midnight blue', command=runrinstr, width = 20).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    # Create a widget button to external resources
    b2 = Button(root, text = 'External Resources', bg='SlateGray2', fg='midnight blue', command=mothurresources, width = 20).pack(anchor=CENTER)
    space2_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    # Create a Button Widget to open files
    button_file = Button(root, text="Preview a Text File", bg='SlateGray2', fg='midnight blue', command= openfile, width = 20).pack(anchor=CENTER)
    space4_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    #Create a Button Widget for bibliography
    button1 = Button(root, text="Project Authors", bg='SlateGray2', fg='midnight blue', command= biblio, width = 20).pack(anchor=CENTER)
    space5_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    #Create a Button Widget to exit the MOTHUR GUI Application
    button_quit = Button(root, text="Exit MOTHUR GUI", bg='SlateGray2', fg='midnight blue', command=popup, width = 20).pack(anchor=CENTER)
    space6_lbl = tkinter.Label(root, text = " ").pack(anchor=CENTER)
    #The argument fill=X expands the button along the x axis.


    root.mainloop()



#Start MOTHUR program commands
#Start mothur Instructions
def runmothurinstr():
    def cont1():
        runquest()
        root2.destroy()    
    root2 = tkinter.Toplevel()#makes window
    root2.title("Instructions")
    root2.geometry("300x140")
    instr1_lbl = tkinter.Label(root2, text = '\nPrior to running MOTHUR, \
please ensure\nthat all required files and executables are\nin a single \
folder for ease of use.\n').pack(anchor=CENTER)#instructions
    cont1_button = tkinter.Button(root2, text='Continue', command = cont1).pack(anchor=CENTER)#continue to os used
    spacerm1_lbl = tkinter.Label(root2, text = " ").pack(anchor=CENTER) #add space between buttons

def runquest():
    root2a = tkinter.Toplevel()#makes window
    root2a.title("Run Mode")
    root2a.geometry("400x200")
    instr1_lbl = tkinter.Label(root2a, text = '\nAre you running MOTHUR \
with single button commands,\nas a batch file, or via the command line?\n').pack(anchor=CENTER)#Question
    single_button = tkinter.Button(root2a, text="Single \
Command", command = osused).pack(anchor=CENTER)#continue to single command line mode
    space1_lbl = tkinter.Label(root2a, text = " ").pack(anchor=CENTER) #add space between buttons
    batch_button = tkinter.Button(root2a, text="Batch \
Mode", command = batchmode).pack(anchor=CENTER) #Continue to batch mode
    space2_lbl = tkinter.Label(root2a, text = " ").pack(anchor=CENTER) #add space between buttons
    command_button = tkinter.Button(root2a, text="Command Line \
Mode", command = commandmode).pack(anchor=CENTER) #Continue to command line mode
    space2_lbl = tkinter.Label(root2a, text = " ").pack(anchor=CENTER) #add space between buttons    

def osused():
    def cont2():   
        global osval
        osval = osrb.get()
        if 1 <= osval <= 3:
            numproc()
            root3.destroy()
        else:            
            messagebox.showinfo("Error", "Please select one of the OS")
            root3.destroy()
            osused()
    root3 = tkinter.Toplevel()#makes window
    root3.title("OS Used")
    root3.geometry("300x225")
    osrb = tkinter.IntVar()
    os_lbl = tkinter.Label(root3, text = "\t\t\nPlease select your operating \
system\nfrom the buttons below\nthen click continue.").pack(anchor=CENTER) #Operating System instructions
    rbwin = tkinter.Radiobutton(root3, text="Windows", variable=osrb, value=1).pack()
    rbosx = tkinter.Radiobutton(root3, text="OSX", variable=osrb, value=2).pack()
    rblin = tkinter.Radiobutton(root3, text="Linux", variable=osrb, value=3).pack()
    spacerm1_lbl = tkinter.Label(root3, text = " ").pack(anchor=CENTER) #add space between buttons
    ont2_button = tkinter.Button(root3, text='Continue', command = cont2).pack(anchor=CENTER)#cont to num of processors.
    spacerm2_lbl = tkinter.Label(root3, text = " ").pack(anchor=CENTER) #add space between buttons

def numproc():
    def cont3():
        global np
        np = procentry.get()
        if np == "":
            messagebox.showinfo("Error", "Please enter an integer value.")
            root4.destroy()
            numproc()
        else:
            np = float(np)
            if np%1 == 0:
                np = int(np)
                root4.destroy()
                setdirectory()
                
            else:            
                messagebox.showinfo("Error", "Please enter an integer value.")
                root4.destroy()
                numproc()                           
    root4 = tkinter.Toplevel()#makes window
    root4.title("Number of Processors")
    proc_lbl = tkinter.Label(root4, text = "\t\t\t\t\t\t\nPlease enter the number of processors\n\
your computer has,\n then click Continue.\n").pack(anchor=CENTER) #Number of processors instructions
    procentry = tkinter.Entry(root4)
    procentry.pack(anchor=CENTER)#Number of processors
    spacerm1_lbl = tkinter.Label(root4, text = " ").pack(anchor=CENTER) #add space between buttons
    setpr_button = tkinter.Button(root4, text='Continue', command = cont3).pack(anchor=CENTER)#sets # of proc and OS used
    spacerm2_lbl = tkinter.Label(root4, text = " ").pack(anchor=CENTER) #add space between buttons

def setdirectory(): #Setting directory to a global variable
    def seldir():
        global dirpath
        try:
            dirpath = filedialog.askdirectory(title = 'Select the Directory')
        except:
            dirpath = dirpath
        if dirpath == "":
            messagebox.showinfo("Error", "Please select a directory.")
        else:
            root5.destroy() 
            mothurcommands()
                   
    root5 = tkinter.Toplevel()
    root5.title("Set Directory")
    opn_lbl = tkinter.Label(root5, text = "\t\t\t\t\t\nPlease navigate to and select\n\
the directory path in which the\nMothur executable file and sequence\n\
files are located.\n").pack(anchor=CENTER)
    opnm_button = tkinter.Button(root5, text='Select Path', command = seldir).pack(anchor=CENTER)#runs seldir which sets cd path
    spacerm1_lbl = tkinter.Label(root5, text = " ").pack(anchor=CENTER) #add space between buttons

def mothurcommands():
    root6 = tkinter.Toplevel()
    root6.title("Single MOTHUR Commands")
    cmd_lbl = tkinter.Label(root6, text = "\nPlease select from \
the following comands\n-----------------------\
---------------------", font=(15)).grid(row=0,column=1)
    desc1_lbl = tkinter.Label(root6, text = "\t\t\t\t\t\nReduce Sequencing and PCR Errors\n").grid(row=1,column=0)
    #button that calls make.file
    makefile_button = tkinter.Button(root6, text = "make.file", command = makefile, width = 20).grid(row=2,column=0)
    #add space between buttons
    spacerm2_lbl = tkinter.Label(root6, text = " ").grid(row=3,column=0) 
    #button that calls make.contigs
    makecontigs_button = tkinter.Button(root6, text = "make.contigs", command = makecontigs, width = 20).grid(row=4,column=0) 
    #add space between buttons
    spacerm3_lbl = tkinter.Label(root6, text = " ").grid(row=5,column=0)  
    #button that calls summary.seqs
    summaryseqs_button = tkinter.Button(root6, text = "summary.seqs", command = summaryseqs, width = 20).grid(row=6,column=0)
    #add space between buttons
    spacerm4_lbl = tkinter.Label(root6, text = " ").grid(row=7,column=0)
    #button that calls screen.seqs
    screenseqs_button = tkinter.Button(root6, text = "screen.seqs", command = screenseqs, width = 20).grid(row=8,column=0)
    #add space between buttons
    spacerm5_lbl = tkinter.Label(root6, text = " ").grid(row=9,column=0)
    desc2_lbl = tkinter.Label(root6, text = "\nProcess Improved Sequences\n").grid(row=1,column=1)
    #button that calls unique.seqs
    uniqueseqs_button = tkinter.Button(root6, text = "unique.seqs", command = uniqueseqs, width = 20).grid(row=2,column=1)
    #add space between buttons
    spacerm6_lbl = tkinter.Label(root6, text = " ").grid(row=3,column=1)
    #button that calls count.seqs
    countseqs_button = tkinter.Button(root6, text = "count.seqs", command = countseqs, width = 20).grid(row=4,column=1)
    #add space between buttons
    spacerm7_lbl = tkinter.Label(root6, text = " ").grid(row=5,column=1)
    #button that calls pcr.seqs
    pcrseqs_button = tkinter.Button(root6, text = "pcr.seqs", command = pcrseqs, width = 20).grid(row=6,column=1)
    #add space between buttons
    spacerm8_lbl = tkinter.Label(root6, text = " ").grid(row=7,column=1)
    #button that calls rename.file
    renamefile_button = tkinter.Button(root6, text = "rename.file", command = renamefile, width = 20).grid(row=8,column=1)
    #add space between buttons
    spacerm9_lbl = tkinter.Label(root6, text = " ").grid(row=9,column=1)
    #button that calls align.seqs
    alignseqs_button = tkinter.Button(root6, text = "align.seqs", command = alignseqs, width = 20).grid(row=10,column=1)
    #add space between buttons
    spacerm10_lbl = tkinter.Label(root6, text = " ").grid(row=11,column=1)
    #button that calls filter.seqs
    filterseqs_button = tkinter.Button(root6, text = "filter.seqs", command = filterseqs, width = 20).grid(row=12,column=1)
    #add space between buttons
    spacerm11_lbl = tkinter.Label(root6, text = " ").grid(row=13,column=1)
    #button that calls pre.cluster
    precluster_button = tkinter.Button(root6, text = "pre.cluster", command = precluster, width = 20).grid(row=14,column=1)
    #add space between buttons
    spacerm12_lbl = tkinter.Label(root6, text = " ").grid(row=15,column=1)
    #button that calls chimera.vsearch
    chimeravsearch_button = tkinter.Button(root6, text = "chimera.vsearch", command = chimeravsearch, width = 20).grid(row=16,column=1)
    #add space between buttons
    spacerm13_lbl = tkinter.Label(root6, text = " ").grid(row=17,column=1)
    #button that calls remove.seqs
    removeseqs_button = tkinter.Button(root6, text = "remove.seqs", command = removeseqs, width = 20).grid(row=18,column=1)
    #add space between buttons
    spacerm14_lbl = tkinter.Label(root6, text = " ").grid(row=19,column=1)
    #button that calls classify.seqs
    classifyseqs_button = tkinter.Button(root6, text = "classify.seqs", command = classifyseqs, width = 20).grid(row=20,column=1)
    #add space between buttons
    spacerm15_lbl = tkinter.Label(root6, text = " ").grid(row=21,column=1)
    #button that calls remove.lineage
    removelineage_button = tkinter.Button(root6, text = "remove.lineage", command = removelineage, width = 20).grid(row=22,column=1)
    #add space between buttons
    spacerm16_lbl = tkinter.Label(root6, text = " ").grid(row=23,column=1)
    #button that calls summary.tax
    summarytax_button = tkinter.Button(root6, text = "summary.tax", command = summarytax, width = 20).grid(row=24,column=1)
    #add space between buttons
    spacerm17_lbl = tkinter.Label(root6, text = " ").grid(row=25,column=1)
    desc2_lbl = tkinter.Label(root6, text = "\t\t\t\t\t\nAssessing Error Rates, Clustering,\n\
and Phylogenetic Trees\n").grid(row=1,column=2)
    #button that calls get.groups
    getgroups_button = tkinter.Button(root6, text = "get.groups", command = getgroups, width = 20).grid(row=2,column=2)
    #add space between buttons
    spacerm18_lbl = tkinter.Label(root6, text = " ").grid(row=3,column=2)
    #button that calls seq.error
    seqerror_button = tkinter.Button(root6, text = "seq.error", command = seqerror, width = 20).grid(row=4,column=2)
    #add space between buttons
    spacerm19_lbl = tkinter.Label(root6, text = " ").grid(row=5,column=2)
    #button that calls dist.seqs
    distseqs_button = tkinter.Button(root6, text = "dist.seqs", command = distseqs, width = 20).grid(row=6,column=2)
    #add space between buttons
    spacerm20_lbl = tkinter.Label(root6, text = " ").grid(row=7,column=2)
    #button that calls cluster
    cluster_button = tkinter.Button(root6, text = "cluster", command = cluster, width = 20).grid(row=8,column=2)
    #add space between buttons
    spacerm21_lbl = tkinter.Label(root6, text = " ").grid(row=9,column=2)
    #button that calls make.shared
    makeshared_button = tkinter.Button(root6, text = "make.shared", command = makeshared, width = 20).grid(row=10,column=2)
    #add space between buttons
    spacerm22_lbl = tkinter.Label(root6, text = " ").grid(row=11,column=2)
    #button that calls rarefaction.single
    rarefactionsingle_button = tkinter.Button(root6, text = "rarefaction.single", command = rarefactionsingle, width = 20).grid(row=12,column=2)
    #add space between buttons
    spacerm23_lbl = tkinter.Label(root6, text = " ").grid(row=13,column=2)
    #button that calls remove.groups
    removegroups_button = tkinter.Button(root6, text = "remove.groups", command = removegroups, width = 20).grid(row=14,column=2)
    #add space between buttons
    spacerm24_lbl = tkinter.Label(root6, text = " ").grid(row=15,column=2)
    #button that calls cluster.split
    clustersplit_button = tkinter.Button(root6, text = "cluster.split", command = clustersplit, width = 20).grid(row=16,column=2)
    #add space between buttons
    spacerm25_lbl = tkinter.Label(root6, text = " ").grid(row=17,column=2)
    #button that calls classify.otu
    classifyotu_button = tkinter.Button(root6, text = "classify.otu", command = classifyotu, width = 20).grid(row=18,column=2)
    #add space between buttons
    spacerm26_lbl = tkinter.Label(root6, text = " ").grid(row=19,column=2)
    #button that calls phylotype
    phylotype_button = tkinter.Button(root6, text = "phylotype", command = phylotype, width = 20).grid(row=20,column=2)
    #add space between buttons
    spacerm27_lbl = tkinter.Label(root6, text = " ").grid(row=21,column=2)
    #button that calls clearcut
    clearcut_button = tkinter.Button(root6, text = "clearcut", command = clearcut, width = 20).grid(row=22,column=2)
    #add space between buttons
    spacerm28_lbl = tkinter.Label(root6, text = " ").grid(row=23,column=2)

    #button that closes window
    close_button = tkinter.Button(root6, text = "Close", command = root6.destroy, width = 20).grid(row=24,column=0)






def selectglobalfile(gftype):
    global gfile
    gfile = ""
    try:
        gfile = filedialog.askopenfilename(title = 'Select the ' + gftype + ' File', filetypes = ( ("\
Files", ("*." + gftype)), ("All files", "*.*" ) ) )
    except:
        gfile = ""

def selectglobalfile2(gftype2):
    global gfile2
    gfile2 = ""
    try:
        gfile2 = filedialog.askopenfilename(title = 'Select the ' + gftype2 + ' File', filetypes = ( ("\
Files", ("*." + gftype2)), ("All files", "*.*" ) ) )
    except:
        gfile2 = ""

def selectglobalfile3(gftype3):
    global gfile3
    gfile3 = ""
    try:
        gfile3 = filedialog.askopenfilename(title = 'Select the ' + gftype3 + ' File', filetypes = ( ("\
Files", ("*." + gftype3)), ("All files", "*.*" ) ) )
    except:
        gfile3 = ""

def selectglobalfile4(gftype4):
    global gfile4
    gfile4 = ""
    try:
        gfile4 = filedialog.askopenfilename(title = 'Select the ' + gftype4 + ' File', filetypes = ( ("\
Files", ("*." + gftype4)), ("All files", "*.*" ) ) )
    except:
        gfile4 = ""

   
def makefile():
    def makefile2():
        global dirpath
        ftvals = ['fastq', 'gz']
        ftypeval = ftyperb.get()
        prefname = prefixentry.get()
        if 1<= ftypeval <=2:
            ft = ftvals[ftypeval - 1]
            if not prefname:
                prefname = 'stability'
            else: prefname = prefname
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('make.file(inputdir=., type=' + ft + ', prefix=' + prefname + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6a.destroy()   
        else:
            messagebox.showinfo("Error", "Please select one of the filetypes")          
    root6a = tkinter.Toplevel()
    root6a.title('make.file')
    ftyperb = tkinter.IntVar()
    ftype_lbl = tkinter.Label(root6a, text = "\t\t\t\t\t\nPlease \
select the file type.").pack(anchor=CENTER) #select file type
    rbfasta = tkinter.Radiobutton(root6a, text="FASTQ", variable=ftyperb, value=1).pack()
    rbgz = tkinter.Radiobutton(root6a, text="GZ", variable=ftyperb, value=2).pack()
    prefix_lbl = tkinter.Label(root6a, text = '\nPlease enter the prefix, if none is\n\
entered the default is "stability"').pack(anchor=CENTER)
    prefixentry = tkinter.Entry(root6a)
    prefixentry.pack(anchor=CENTER)#Prefix
    spacerm1_lbl = tkinter.Label(root6a, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6a, text='Continue', command = makefile2).pack(anchor=CENTER)#make.file button.
    spacerm2_lbl = tkinter.Label(root6a, text = " ").pack(anchor=CENTER) #add space
    
def makecontigs():
    def ftypedisplay():
        selectglobalfile("files")
    def makecontigs2():
        global dirpath
        global np
        global gfile
        if gfile == "":
            messagebox.showinfo("Error", "Please select the file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('make.contigs(file=' + gfile + ', processors=' + str(np) + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6b.destroy() 
    global gfile
    gfile = ""
    root6b = tkinter.Toplevel()
    root6b.title('make.contigs')
    mcfile_lbl = tkinter.Label(root6b, text = '\t\t\t\t\t\nPlease select the file to use.').pack(anchor=CENTER)
    mcf1_button = tkinter.Button(root6b, text='Select File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6b, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6b, text='Continue', command = makecontigs2).pack(anchor=CENTER)#make.contigs button.
    spacerm2_lbl = tkinter.Label(root6b, text = " ").pack(anchor=CENTER) #add space

def summaryseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def summaryseqs2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        else:
            if gfile2 == "":
                countfile = ""
                commas = ''
            else:
                countfile = ('count=' + gfile2)
                commas = ', '
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('summary.seqs(fasta=' + gfile + commas + countfile + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6c.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6c = tkinter.Toplevel()
    root6c.title('summary.seqs')
    ssfile_lbl = tkinter.Label(root6c, text = '\t\t\t\t\t\nPlease select the Fasta file location\n\
and Count file if needed.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6c, text="Select Fasta File (req'd)", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6c, text = " ").pack(anchor=CENTER) #add space between buttons
    ss1_button = tkinter.Button(root6c, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6c, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6c, text='Continue', command = summaryseqs2).pack(anchor=CENTER)#summary.seqs button.
    spacerm2_lbl = tkinter.Label(root6c, text = " ").pack(anchor=CENTER) #add space

def screenseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("groups")
    def ftypedisplay3():
        selectglobalfile3("count_table")
    def ftypedisplay4():
        selectglobalfile4("summary")
    def screenseqs2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        global gfile4
        maxamb = maxambentry.get()
        maxlen = maxlenentry.get()
        maxh = maxhomopentry.get()
        spos = startposentry.get()
        epos = endposentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select a fasta file.")
        else:
            if gfile2 == "":
                group = ''
            else:
                group = ', group=' + gfile2                
            if gfile3 == "":
                count = ''
            else:
                count = ', count=' + gfile3
            if gfile4 == "":
                summary = ''
            else:
                summary = ', summary=' + gfile4
            if maxamb == "":
                maxambig = ''
            else:
                maxambig = ', maxambig=' + str(maxamb)
            if maxlen == "":
                maxlength = ''
            else:
                maxlength = ', maxlength=' + str(maxlen)
            if maxh == "":
                maxhomop = ''
            else:
                maxhomop = ', maxhomop=' + str(maxh)
            if spos == "":
                start = ''
            else:
                start = ', start=' + str(spos)
            if epos == "":
                end = ''
            else:
                end = ', end=' + str(epos)                
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('screen.seqs(fasta=' + gfile + group + count + summary +\
                    maxambig + maxlength + start + end + maxhomop + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6d.destroy()
    global gfile
    global gfile2
    global gfile3
    global gfile4
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    gfile4 = ""
    root6d = tkinter.Toplevel()
    root6d.title('screen.seqs')
    ssfile1_lbl = tkinter.Label(root6d, text = '\t\t\t\t\t\nPlease select the Fasta file location.').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6d, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6d, text = " ").pack(anchor=CENTER) #add space between buttons
    ssfile2_lbl = tkinter.Label(root6d, text = '\nPlease select the rest of the\nfiles as needed.').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6d, text='Select Groups File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ssf3_button = tkinter.Button(root6d, text='Select Count File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.
    ssf4_button = tkinter.Button(root6d, text='Select Summary File', command = ftypedisplay4).pack(anchor=CENTER)#Select the file button.
    ssfile3_lbl = tkinter.Label(root6d, text = '\nPlease enter the\nfollowing parameters as needed.').pack(anchor=CENTER)
    ssfile3_lbl = tkinter.Label(root6d, text = '\nMax Ambiguity.').pack(anchor=CENTER)
    maxambentry = tkinter.Entry(root6d)
    maxambentry.pack(anchor=CENTER)#max ambiguity
    ssfile4_lbl = tkinter.Label(root6d, text = '\nMax Length.').pack(anchor=CENTER)
    maxlenentry = tkinter.Entry(root6d)
    maxlenentry.pack(anchor=CENTER)#max length
    ssfile5_lbl = tkinter.Label(root6d, text = '\nMax Homopolymer.').pack(anchor=CENTER)
    maxhomopentry = tkinter.Entry(root6d)
    maxhomopentry.pack(anchor=CENTER)#max homopolymer
    ssfile6_lbl = tkinter.Label(root6d, text = '\nStart Position.').pack(anchor=CENTER)
    startposentry = tkinter.Entry(root6d)
    startposentry.pack(anchor=CENTER)#start position
    ssfile7_lbl = tkinter.Label(root6d, text = '\nEnd Position.').pack(anchor=CENTER)
    endposentry = tkinter.Entry(root6d)
    endposentry.pack(anchor=CENTER)#end position    
    spacerm3_lbl = tkinter.Label(root6d, text = " ").pack(anchor=CENTER) #add space
    cont_button = tkinter.Button(root6d, text='Continue', command = screenseqs2).pack(anchor=CENTER)#screen.seqs button.
    spacerm4_lbl = tkinter.Label(root6d, text = " ").pack(anchor=CENTER) #add space

def uniqueseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")       
    def uniqueseqs2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select a fasta file.")
        else:
            if gfile2 == "":
                count = ''
            else:
                count = ', count=' + gfile2                 
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('unique.seqs(fasta=' + gfile + count + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6e.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6e = tkinter.Toplevel()
    root6e.title('unique.seqs')
    ssfile1_lbl = tkinter.Label(root6e, text = '\t\t\t\t\t\nPlease select the\
Fasta file and Count file if needed.').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6e, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6e, text = " ").pack(anchor=CENTER) #add space between buttons
    ssf1_button = tkinter.Button(root6e, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6e, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6e, text='Continue', command = uniqueseqs2).pack(anchor=CENTER)#screen.seqs button.
    spacerm3_lbl = tkinter.Label(root6e, text = " ").pack(anchor=CENTER) #add space

def countseqs():
    def ftypedisplay():
        selectglobalfile("names")
    def ftypedisplay2():
        selectglobalfile2("groups")
    def countseqs2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select a names file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select a groups file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('count.seqs(name=' + gfile + ', group=' + gfile2 + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6f.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6f = tkinter.Toplevel()
    root6f.title('count.seqs')
    ssfile1_lbl = tkinter.Label(root6f, text = '\t\t\t\t\t\nPlease select the Names file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6f, text='Select Names File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ssfile2_lbl = tkinter.Label(root6f, text = '\nPlease select the Groups file location').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6f, text='Select Groups File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6f, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6f, text='Continue', command = countseqs2).pack(anchor=CENTER)#count.seqs button.
    spacerm2_lbl = tkinter.Label(root6f, text = " ").pack(anchor=CENTER) #add space

def pcrseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def pcrseqs2():
        global dirpath
        global gfile
        global np
        startpos = startposentry.get()
        endpos = endposentry.get()
        keepdotval = keepdotrb.get()        
        if gfile == "":
            messagebox.showinfo("Error", "Please select a fasta file.")
        else:
            if startpos != "" :
                starttext = (', start=' + str(startpos))
            else:
                starttext = ""
            if endpos != "":
                endtext = (', end=' + str(endpos))
            else:
                endtext = ""
            if keepdotval == 1:
                dotkeep = ', keepdots=T'
            elif keepdotval ==2:
                dotkeep = ', keepdots=F'
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('pcr.seqs(fasta=' + gfile + starttext + endtext + dotkeep + ', processors=' + str(np) + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6g.destroy()
    global gfile
    gfile = ""
    root6g = tkinter.Toplevel()
    root6g.title('pcr.seqs')
    ssfile1_lbl = tkinter.Label(root6g, text = '\t\t\t\t\t\nPlease select the Fasta file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6g, text='Select fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6g, text = " ").pack(anchor=CENTER) #add space between buttons
    ssfile3_lbl = tkinter.Label(root6g, text = '\nIf needed, please enter the\n\
starting position to trim from.').pack(anchor=CENTER)
    startposentry = tkinter.Entry(root6g)
    startposentry.pack(anchor=CENTER)#start trim position
    ssfile4_lbl = tkinter.Label(root6g, text = '\nIf needed, please enter the\n\
ending position to trim from.').pack(anchor=CENTER)
    endposentry = tkinter.Entry(root6g)
    endposentry.pack(anchor=CENTER)#end trim position
    keepdotrb = tkinter.IntVar()
    keepdotrb.set(1)
    keepdots_lbl = tkinter.Label(root6g, text = "\nKeep the leading and trailing .’s?\n\
default=True.").pack(anchor=CENTER) #keep dots?
    rbdotstrue = tkinter.Radiobutton(root6g, text="True", variable=keepdotrb, value=1).pack()
    rbdotsfalse = tkinter.Radiobutton(root6g, text="False", variable=keepdotrb, value=2).pack()
    spacerm2_lbl = tkinter.Label(root6g, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6g, text='Continue', command = pcrseqs2).pack(anchor=CENTER)#pcr.seqs button.
    spacerm3_lbl = tkinter.Label(root6g, text = " ").pack(anchor=CENTER) #add space

def renamefile():
    def ftypedisplay():
        selectglobalfile("fasta")
    def renamefile2():
        global dirpath
        global gfile
        newname = newnameentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select a file to rename.")
        elif newname == "":
            messagebox.showinfo("Error", "Please enter the new file name.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('rename.file(input=' + gfile + ', new=' + newname +  ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6h.destroy()
    global gfile
    gfile = ""
    root6h = tkinter.Toplevel()
    root6h.title('rename.file')
    newname_lbl = tkinter.Label(root6h, text = '\t\t\t\t\t\nPlease select the location of the file to rename').pack(anchor=CENTER)
    sf_button = tkinter.Button(root6h, text='Select File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    newname_lbl = tkinter.Label(root6h, text = '\nPlease enter the new file name.').pack(anchor=CENTER)
    newnameentry = tkinter.Entry(root6h)
    newnameentry.pack(anchor=CENTER)#new file name
    spacerm1_lbl = tkinter.Label(root6h, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6h, text='Continue', command = renamefile2).pack(anchor=CENTER)#rename.file button.
    spacerm3_lbl = tkinter.Label(root6h, text = " ").pack(anchor=CENTER) #add space

def alignseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("fasta")
    def alignseqs2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select a Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select a Reference file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('align.seqs(fasta=' + gfile + ', reference=' + gfile2 + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6i.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6i = tkinter.Toplevel()
    root6i.title('align.seqs')
    ssfile1_lbl = tkinter.Label(root6i, text = '\t\t\t\t\t\nPlease select the Fasta file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6i, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ssfile2_lbl = tkinter.Label(root6i, text = '\nPlease select the Reference file location').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6i, text='Select Reference File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm2_lbl = tkinter.Label(root6i, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6i, text='Continue', command = alignseqs2).pack(anchor=CENTER)#align.seqs button.
    spacerm3_lbl = tkinter.Label(root6i, text = " ").pack(anchor=CENTER) #add space
        
def filterseqs():
    def ftypedisplay():
        selectglobalfile("align")
    def filterseqs2():
        global dirpath
        global gfile
        global np
        trumpchar = trumpentry.get()
        vertval = verticalrb.get()        
        if gfile == "":
            messagebox.showinfo("Error", "Please select a file.")
        else:
            if trumpchar != "" :
                trumptext = (', trump=' + str(trumpchar))
            else:
                trumptext = ""
            if vertval == 1:
                verttext = ', vertical=T'
            elif vertval ==2:
                verttext = ', vertical=F'
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('filter.seqs(fasta=' + gfile + verttext + trumptext + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6j.destroy()
    global gfile
    gfile = ""
    root6j = tkinter.Toplevel()
    root6j.title('filter.seqs')
    ffile1_lbl = tkinter.Label(root6j, text = '\t\t\t\t\t\nPlease select the file.').pack(anchor=CENTER)
    ffile1_button = tkinter.Button(root6j, text='Select File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6j, text = " ").pack(anchor=CENTER) #add space between buttons
    trump_lbl = tkinter.Label(root6j, text = '\nIf needed, please enter the\n\
trump character (e.g. .)').pack(anchor=CENTER)
    trumpentry = tkinter.Entry(root6j)
    trumpentry.pack(anchor=CENTER)#trump character
    verticalrb = tkinter.IntVar()
    verticalrb.set(1)
    vertical_lbl = tkinter.Label(root6j, text = "\nVertical? \
default=True.").pack(anchor=CENTER) #keep dots?
    rbdotstrue = tkinter.Radiobutton(root6j, text="True", variable=verticalrb, value=1).pack()
    rbdotsfalse = tkinter.Radiobutton(root6j, text="False", variable=verticalrb, value=2).pack()
    spacerm2_lbl = tkinter.Label(root6j, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6j, text='Continue', command = filterseqs2).pack(anchor=CENTER)#filter.seqs button.
    spacerm3_lbl = tkinter.Label(root6j, text = " ").pack(anchor=CENTER) #add space

def precluster():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def precluster2():
        global dirpath
        global gfile
        global gfile2
        dif = difnumentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif dif == "":
            messagebox.showinfo("Error", "Please enter the max allowed differences.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('pre.cluster(fasta=' + gfile + ', count=' + gfile2 + ', diffs=' + str(dif) + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6k.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6k = tkinter.Toplevel()
    root6k.title('pre.cluster')
    pcinst1_lbl = tkinter.Label(root6k, text = '\t\t\t\t\t\nPlease select the Fasta file\n\
and Count file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6k, text="Select Fasta File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6k, text = " ").pack(anchor=CENTER) #add space between buttons
    ss1_button = tkinter.Button(root6k, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    pcinst2_lbl = tkinter.Label(root6k, text = '\nPlease enter the max number\n\
of differences allowed.').pack(anchor=CENTER)
    difnumentry = tkinter.Entry(root6k)
    difnumentry.pack(anchor=CENTER)#max differences
    spacerm2_lbl = tkinter.Label(root6k, text = " ").pack(anchor=CENTER) #add space
    cont_button = tkinter.Button(root6k, text='Continue', command = precluster2).pack(anchor=CENTER)#pre.cluster button.
    spacerm3_lbl = tkinter.Label(root6k, text = " ").pack(anchor=CENTER) #add space

def chimeravsearch():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def chimeravsearch2():
        global dirpath
        global gfile
        global gfile2
        derepval = dereprb.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        else:
            if derepval == 1:
                derep = 't'
            else:
                derep = 'f'
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('chimera.vsearch(fasta=' + gfile + ', count=' + gfile2 + ', dereplicate=' + derep + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6l.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6l = tkinter.Toplevel()
    root6l.title('chimera.vsearch')
    pcinst1_lbl = tkinter.Label(root6l, text = '\t\t\t\t\t\nPlease select the Fasta file\n\
and Count file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6l, text="Select Fasta File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6l, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    dereprb = tkinter.IntVar()
    dereprb.set(2)
    derep_lbl = tkinter.Label(root6l, text = "\nDereplicate? \
default=False.").pack(anchor=CENTER) #Dereplicate?
    dereptruerb = tkinter.Radiobutton(root6l, text="True", variable=dereprb, value=1).pack()
    derepfalserb = tkinter.Radiobutton(root6l, text="False", variable=dereprb, value=2).pack()
    cont_button = tkinter.Button(root6l, text='Continue', command = chimeravsearch2).pack(anchor=CENTER)#chimera.vsearch button.
    spacerm2_lbl = tkinter.Label(root6l, text = " ").pack(anchor=CENTER) #add space

def removeseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("accnos")
    def removeseqs2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select a Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select an Accnos file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('remove.seqs(fasta=' + gfile + ', accnos=' + gfile2 + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6m.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6m = tkinter.Toplevel()
    root6m.title('remove.seqs')
    ssfile1_lbl = tkinter.Label(root6m, text = '\t\t\t\t\t\nPlease select the Fasta file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6m, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ssfile2_lbl = tkinter.Label(root6m, text = '\nPlease select the Accnos file location').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6m, text='Select Accnos File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6m, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6m, text='Continue', command = removeseqs2).pack(anchor=CENTER)#remove.seqs button.
    spacerm2_lbl = tkinter.Label(root6m, text = " ").pack(anchor=CENTER) #add space

def classifyseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def ftypedisplay3():
        selectglobalfile3("fasta")
    def ftypedisplay4():
        selectglobalfile4("tax")
    def classifyseqs2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        global gfile4
        cutoffval = cutoffentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select a Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select an Count file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select an Reference file.")
        elif gfile4 == "":
            messagebox.showinfo("Error", "Please select an Tax file.")
        else:
            if cutoffval == "":
                cutoffnum = 80
            else:
                cutoffnum = cutoffval
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('classify.seqs(fasta=' + gfile + ', count=' + gfile2 + ', reference=' + gfile3 + ', taxonomy=' + gfile4 + ', cutoff=' + str(cutoffnum) + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6n.destroy()
    global gfile
    global gfile2
    global gfile3
    global gfile4
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    gfile4 = ""
    root6n = tkinter.Toplevel()
    root6n.title('classify.seqs')
    ssfile1_lbl = tkinter.Label(root6n, text = '\t\t\t\t\t\nPlease select the Fasta file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6n, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ssfile2_lbl = tkinter.Label(root6n, text = '\nPlease select the Count file location').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6n, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ssfile3_lbl = tkinter.Label(root6n, text = '\nPlease select the Reference file location').pack(anchor=CENTER)
    ssf4_button = tkinter.Button(root6n, text='Select Reference File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.
    ssfile4_lbl = tkinter.Label(root6n, text = '\nPlease select the Tax file location').pack(anchor=CENTER)
    ssf4_button = tkinter.Button(root6n, text='Select Tax File', command = ftypedisplay4).pack(anchor=CENTER)#Select the file button.
    pcinst2_lbl = tkinter.Label(root6n, text = '\nPlease enter the cutoff value\n\
default=80.').pack(anchor=CENTER)
    cutoffentry = tkinter.Entry(root6n)
    cutoffentry.pack(anchor=CENTER)#cutoff  
    spacerm1_lbl = tkinter.Label(root6n, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6n, text='Continue', command = classifyseqs2).pack(anchor=CENTER)#classify.seqs button.
    spacerm2_lbl = tkinter.Label(root6n, text = " ").pack(anchor=CENTER) #add space
        
def removelineage():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def ftypedisplay3():
        selectglobalfile3("taxonomy")
    def removelineage2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        taxon = taxonentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select a Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select an Count file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select an Taxonomy file.")
        elif taxon == "":
            messagebox.showinfo("Error", "Please enter the taxon(s) to remove.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('remove.lineage(fasta=' + gfile + ', count=' + gfile2 + ', taxonomy=' + gfile3 + ', taxon=' + taxon + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6o.destroy()
    global gfile
    global gfile2
    global gfile3
    global gfile4
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    gfile4 = ""
    root6o = tkinter.Toplevel()
    root6o.title('remove.lineage')
    ssfile1_lbl = tkinter.Label(root6o, text = '\t\t\t\t\t\nPlease select the Fasta file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6o, text='Select Fasta File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ssfile2_lbl = tkinter.Label(root6o, text = '\nPlease select the Count file location').pack(anchor=CENTER)
    ssf2_button = tkinter.Button(root6o, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ssfile3_lbl = tkinter.Label(root6o, text = '\nPlease select the Taxonomy file location').pack(anchor=CENTER)
    ssf3_button = tkinter.Button(root6o, text='Select Taxonomy File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.
    taxinst_lbl = tkinter.Label(root6o, text = '\nPlease enter the taxon(s) to remove\n\
separated by a "-" sign as appropriate.').pack(anchor=CENTER)
    taxonentry = tkinter.Entry(root6o)
    taxonentry.pack(anchor=CENTER)#cutoff  
    spacerm2_lbl = tkinter.Label(root6o, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6o, text='Continue', command = removelineage2).pack(anchor=CENTER)#remove.lineage button.
    spacerm3_lbl = tkinter.Label(root6o, text = " ").pack(anchor=CENTER) #add space

def summarytax():
    def ftypedisplay():
        selectglobalfile("taxonomy")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def summarytax2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        else:
            if gfile2 == "":
                countfile = ""
                commas = ''
            else:
                countfile = ('count=' + gfile2)
                commas = ', '
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('summary.tax(taxonomy=' + gfile + commas + countfile + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6p.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6p = tkinter.Toplevel()
    root6p.title('summary.tax')
    ssfile_lbl = tkinter.Label(root6p, text = '\t\t\t\t\t\nPlease select the Taxonomy file location\n\
and Count file if needed.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6p, text="Select Taxonomy File (req'd)", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6p, text = " ").pack(anchor=CENTER) #add space between buttons
    ss1_button = tkinter.Button(root6p, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6p, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6p, text='Continue', command = summarytax2).pack(anchor=CENTER)#summary.tax button.
    spacerm2_lbl = tkinter.Label(root6p, text = " ").pack(anchor=CENTER) #add space

def getgroups():
    def ftypedisplay():
        selectglobalfile("count_table")
    def ftypedisplay2():
        selectglobalfile2("fasta")
    def getgroups2():
        global dirpath
        global gfile
        global gfile2
        global osval
        groupval = groupentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif groupval == "":
            messagebox.showinfo("Error", "Please enter the Groups.")
        else:
            if osval == 1:
                group = groupval.upper()
            else:
                group = groupval
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('get.groups(count=' + gfile + ', fasta=' + gfile2 + ', groups=' + group + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6q.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6q = tkinter.Toplevel()
    root6q.title('get.groups')
    pcinst1_lbl = tkinter.Label(root6q, text = '\t\t\t\t\t\nPlease select the Count file\n\
and Fasta file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6q, text="Select Count File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6q, text='Select Fasta File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    groups_lbl = tkinter.Label(root6q, text = "\nPlease enter the Groups.").pack(anchor=CENTER)
    groupentry = tkinter.Entry(root6q)
    groupentry.pack(anchor=CENTER)#groups 
    spacerm1_lbl = tkinter.Label(root6q, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6q, text='Continue', command = getgroups2).pack(anchor=CENTER)#get.groups button.
    spacerm2_lbl = tkinter.Label(root6q, text = " ").pack(anchor=CENTER) #add space

def seqerror():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def ftypedisplay3():
        selectglobalfile3("fasta")
    def seqerror2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        alignedval = alignedrb.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select the Reference file.")
        else:
            if alignedval == 1:
                align = 'T'
            elif alignedval ==2:
                align = 'F'
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('seq.error(fasta=' + gfile + ', count=' + gfile2 + ', reference=' + gfile3 + ', aligned=' + align + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6r.destroy()
    global gfile
    global gfile2
    global gfile3
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    root6r = tkinter.Toplevel()
    root6r.title('seq.error')
    pcinst1_lbl = tkinter.Label(root6r, text = '\t\t\t\t\t\nPlease select the Fasta,\n\
Count, and Reference File locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6r, text="Select Fasta File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6r, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6r, text='Select Reference File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.
    alignedrb = tkinter.IntVar()
    alignedrb.set(2)
    aligned_lbl = tkinter.Label(root6r, text = "\nAligned? \
default=False.").pack(anchor=CENTER) #Dereplicate?
    alignedtruerb = tkinter.Radiobutton(root6r, text="True", variable=alignedrb, value=1).pack()
    alignedfalserb = tkinter.Radiobutton(root6r, text="False", variable=alignedrb, value=2).pack()
    cont_button = tkinter.Button(root6r, text='Continue', command = seqerror2).pack(anchor=CENTER)#seq.error button.
    spacerm2_lbl = tkinter.Label(root6r, text = " ").pack(anchor=CENTER) #add space

def distseqs():
    def ftypedisplay():
        selectglobalfile("fasta")
    def distseqs2():
        global dirpath
        global gfile
        coff = coffentry.get()
        out = outentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        else:
            if coff == "":
                cutoff = ''
            else:
                cutoff = ', cutoff=' + str(coff)
            if out == "":
                output = ''
            else:
                output = ', output=' + str(out)          
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('dist.seqs(fasta=' + gfile + cutoff + output + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6s.destroy()
    global gfile
    gfile = ""
    root6s = tkinter.Toplevel()
    root6s.title('dist.seqs')
    inst1_lbl = tkinter.Label(root6s, text = '\t\t\t\t\t\nPlease select the\n\
Fasta file location.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6s, text="Select Fasta File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    inst2_lbl = tkinter.Label(root6s, text = '\nPlease enter the following\nparameters as needed.\n\nCutoff.').pack(anchor=CENTER)
    coffentry = tkinter.Entry(root6s)
    coffentry.pack(anchor=CENTER)#cutoff
    inst3_lbl = tkinter.Label(root6s, text = '\nOutput.').pack(anchor=CENTER)
    outentry = tkinter.Entry(root6s)
    outentry.pack(anchor=CENTER)#output
    spacerm2_lbl = tkinter.Label(root6s, text = " ").pack(anchor=CENTER) #add space
    cont_button = tkinter.Button(root6s, text='Continue', command = distseqs2).pack(anchor=CENTER)#dist.seqs button.
    spacerm3_lbl = tkinter.Label(root6s, text = " ").pack(anchor=CENTER) #add space

def cluster():
    def ftypedisplay():
        selectglobalfile("dist")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def cluster2():
        global dirpath
        global gfile
        global gfile2
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Column file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('cluster(column=' + gfile + ', count=' + gfile2 + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6t.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6t = tkinter.Toplevel()
    root6t.title('cluster')
    ssfile_lbl = tkinter.Label(root6t, text = '\t\t\t\t\t\nPlease select the Column file\n\
and Count file.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6t, text="Select Column File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6t, text = " ").pack(anchor=CENTER) #add space between buttons
    ss1_button = tkinter.Button(root6t, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6t, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6t, text='Continue', command = cluster2).pack(anchor=CENTER)#mothur cluster button.
    spacerm2_lbl = tkinter.Label(root6t, text = " ").pack(anchor=CENTER) #add space

def makeshared():
    def ftypedisplay():
        selectglobalfile("list")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def makeshared2():
        global dirpath
        global gfile
        global gfile2
        labelval = labelentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the List file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif labelval == "":
            messagebox.showinfo("Error", "Please enter the Label.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('make.shared(list=' + gfile + ', count=' + gfile2 + ', label=' + str(labelval) + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6u.destroy()
    global gfile
    global gfile2
    gfile = ""
    gfile2 = ""
    root6u = tkinter.Toplevel()
    root6u.title('make.shared')
    pcinst1_lbl = tkinter.Label(root6u, text = '\t\t\t\t\t\nPlease select the List file\n\
and Count file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6u, text="Select List File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6u, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    label_lbl = tkinter.Label(root6u, text = "\nPlease enter the Label.").pack(anchor=CENTER)
    labelentry = tkinter.Entry(root6u)
    labelentry.pack(anchor=CENTER)#groups 
    spacerm1_lbl = tkinter.Label(root6u, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6u, text='Continue', command = makeshared2).pack(anchor=CENTER)#make.shared button.
    spacerm2_lbl = tkinter.Label(root6u, text = " ").pack(anchor=CENTER) #add space

def rarefactionsingle():
    def ftypedisplay():
        selectglobalfile("shared")  
    def rarefactionsingle2():
        global dirpath
        global gfile
        if gfile == "":
            messagebox.showinfo("Error", "Please select a Shared file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('rarefaction.single(shared=' + gfile + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6v.destroy()
    global gfile
    gfile = ""
    root6v = tkinter.Toplevel()
    root6v.title('rarefaction.single')
    ssfile1_lbl = tkinter.Label(root6v, text = '\t\t\t\t\t\nPlease select the Shared file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6v, text='Select Shared File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6v, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6v, text='Continue', command = rarefactionsingle2).pack(anchor=CENTER)#rarefaction.single button.
    spacerm3_lbl = tkinter.Label(root6v, text = " ").pack(anchor=CENTER) #add space

def removegroups():
    def ftypedisplay():
        selectglobalfile("count_table")
    def ftypedisplay2():
        selectglobalfile2("fasta")
    def ftypedisplay3():
        selectglobalfile3("taxonomy")
    def removegroups2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        global osval
        groupval = groupentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select the Taxonomy file.")
        elif groupval == "":
            messagebox.showinfo("Error", "Please enter the Groups.")
        else:
            if osval == 1:
                group = groupval.upper()
            else:
                group = groupval
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('remove.groups(count=' + gfile + ', fasta=' + gfile2 +  ', taxonomy=' + gfile3 + ', groups=' + group + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6w.destroy()
    global gfile
    global gfile2
    global gfile3
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    root6w = tkinter.Toplevel()
    root6w.title('remove.groups')
    pcinst1_lbl = tkinter.Label(root6w, text = '\t\t\t\t\t\nPlease select the Count, Fasta,\n\
and Taxonomy file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6w, text="Select Count File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6w, text='Select Fasta File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6w, text='Select Taxonomy File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.
    groups_lbl = tkinter.Label(root6w, text = "\nPlease enter the Groups.").pack(anchor=CENTER)
    groupentry = tkinter.Entry(root6w)
    groupentry.pack(anchor=CENTER)#groups 
    spacerm1_lbl = tkinter.Label(root6w, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6w, text='Continue', command = removegroups2).pack(anchor=CENTER)#remove.groups button.
    spacerm2_lbl = tkinter.Label(root6w, text = " ").pack(anchor=CENTER) #add space

def clustersplit():
    def ftypedisplay():
        selectglobalfile("fasta")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def ftypedisplay3():
        selectglobalfile3("taxonomy")
    def clustersplit2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        global osval
        spmethod = spmethodentry.get()
        taxlevel = taxlevelentry.get()
        cutoff = cutoffentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Fasta file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select the Taxonomy file.")
        elif spmethod == "":
            messagebox.showinfo("Error", "Please enter the Split Method.")
        elif taxlevel == "":
            messagebox.showinfo("Error", "Please enter the Taxonomy Level.")
        elif cutoff == "":
            messagebox.showinfo("Error", "Please enter the Cutoff.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('cluster.split(fasta=' + gfile + ', count=' + gfile2 +  ', taxonomy=' + gfile3 + \
                    ', splitmethod=' + spmethod + ', taxlevel=' + str(taxlevel) + ', cutoff=' + str(cutoff) + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6x.destroy()
    global gfile
    global gfile2
    global gfile3
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    root6x = tkinter.Toplevel()
    root6x.title('cluster.split')
    pcinst1_lbl = tkinter.Label(root6x, text = '\t\t\t\t\t\nPlease select the Count, Fasta,\n\
and Taxonomy file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6x, text="Select Fasta File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6x, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6x, text='Select Taxonomy File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.   
    entry1_lbl = tkinter.Label(root6x, text = "\nPlease enter the Split Method.").pack(anchor=CENTER)
    spmethodentry = tkinter.Entry(root6x)
    spmethodentry.pack(anchor=CENTER)#split method
    entry2_lbl = tkinter.Label(root6x, text = "\nPlease enter the Taxonomy Level.").pack(anchor=CENTER)
    taxlevelentry = tkinter.Entry(root6x)
    taxlevelentry.pack(anchor=CENTER)#taxonomy level
    entry3_lbl = tkinter.Label(root6x, text = "\nPlease enter the Cutoff.").pack(anchor=CENTER)
    cutoffentry = tkinter.Entry(root6x)
    cutoffentry.pack(anchor=CENTER)#cutoff    
    spacerm1_lbl = tkinter.Label(root6x, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6x, text='Continue', command = clustersplit2).pack(anchor=CENTER)#cluster.split button.
    spacerm2_lbl = tkinter.Label(root6x, text = " ").pack(anchor=CENTER) #add space


def classifyotu():
    def ftypedisplay():
        selectglobalfile("list")
    def ftypedisplay2():
        selectglobalfile2("count_table")
    def ftypedisplay3():
        selectglobalfile3("taxonomy")
    def classifyotu2():
        global dirpath
        global gfile
        global gfile2
        global gfile3
        global osval
        label = labelentry.get()
        if gfile == "":
            messagebox.showinfo("Error", "Please select the List file.")
        elif gfile2 == "":
            messagebox.showinfo("Error", "Please select the Count file.")
        elif gfile3 == "":
            messagebox.showinfo("Error", "Please select the Taxonomy file.")
        elif label == "":
            messagebox.showinfo("Error", "Please enter the Label.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('classify.otu(list=' + gfile + ', count=' + gfile2 +  ', taxonomy=' + gfile3 + \
                    ', label=' + str(label) + ')' )
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6y.destroy()
    global gfile
    global gfile2
    global gfile3
    gfile = ""
    gfile2 = ""
    gfile3 = ""
    root6y = tkinter.Toplevel()
    root6y.title('classify.otu')
    pcinst1_lbl = tkinter.Label(root6y, text = '\t\t\t\t\t\nPlease select the List, Count,\n\
and Taxonomy file locations.').pack(anchor=CENTER)
    ss1_button = tkinter.Button(root6y, text="Select List File", command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6y, text='Select Count File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
    ss1_button = tkinter.Button(root6y, text='Select Taxonomy File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button.   
    entry1_lbl = tkinter.Label(root6y, text = "\nPlease enter the Label.").pack(anchor=CENTER)
    labelentry = tkinter.Entry(root6y)
    labelentry.pack(anchor=CENTER)#label    
    spacerm1_lbl = tkinter.Label(root6y, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6y, text='Continue', command = classifyotu2).pack(anchor=CENTER)#classify.otu button.
    spacerm2_lbl = tkinter.Label(root6y, text = " ").pack(anchor=CENTER) #add space

def phylotype():
    def ftypedisplay():
        selectglobalfile("taxonomy")  
    def phylotype2():
        global dirpath
        global gfile
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Taxonomy file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('phylotype(taxonomy=' + gfile + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6z.destroy()
    global gfile
    gfile = ""
    root6z = tkinter.Toplevel()
    root6z.title('phylotype')
    ssfile1_lbl = tkinter.Label(root6z, text = '\t\t\t\t\t\nPlease select the Taxonomy file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6z, text='Select Taxonomy File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6z, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6z, text='Continue', command = phylotype2).pack(anchor=CENTER)#phylotype button.
    spacerm3_lbl = tkinter.Label(root6z, text = " ").pack(anchor=CENTER) #add space

def clearcut():
    def ftypedisplay():
        selectglobalfile("dist")  
    def clearcut2():
        global dirpath
        global gfile
        if gfile == "":
            messagebox.showinfo("Error", "Please select the Distance file.")
        else:
            os.chdir(dirpath) #set directory
            #Make a temp file with the timestamp for uniqueness
            tempmakefile = 'temp' + time.strftime("%Y%m%d-%H%M%S") + '.batch'
            f = open(dirpath + '/' + tempmakefile,'w+') #creates mini batch file
            f.write('clearcut(phylip=' + gfile + ')')
            f.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.system('cmd /k "mothur "' + tempmakefile) #run mini batch file 
            os.remove(dirpath + '/' + tempmakefile) #remove temp file
            root6aa.destroy()
    global gfile
    gfile = ""
    root6aa = tkinter.Toplevel()
    root6aa.title('phylotype')
    ssfile1_lbl = tkinter.Label(root6aa, text = '\t\t\t\t\t\nPlease select the Distance file location').pack(anchor=CENTER)
    ssf1_button = tkinter.Button(root6aa, text='Select Distance File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
    spacerm1_lbl = tkinter.Label(root6aa, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(root6aa, text='Continue', command = clearcut2).pack(anchor=CENTER)#clearcut button.
    spacerm3_lbl = tkinter.Label(root6aa, text = " ").pack(anchor=CENTER) #add space



    

def batchmode():
    def selbatch():
        global gfile
        selectglobalfile("batch")
        if gfile == "":
            messagebox.showinfo("Error", "Please select the\n\
batch file.")
        else:
            batchdir = Path(gfile).parent
            os.chdir(batchdir)
            os.system('cmd /k "mothur "' + gfile)
            root2b.destroy()
    root2b = tkinter.Toplevel()
    root2b.title("Run Batch File")
    opn_lbl = tkinter.Label(root2b, text = "\t\t\t\t\t\nPlease navigate to and select\n\
the batch file.\n").pack(anchor=CENTER)
    opnm_button = tkinter.Button(root2b, text='Select File', command = selbatch).pack(anchor=CENTER)#runs selbatch which selects batch
    spacerm1_lbl = tkinter.Label(root2b, text = " ").pack(anchor=CENTER) #add space 

def commandmode():
    def selmothurexe():
        global gfile
        selectglobalfile("exe")
        if gfile == "":
            messagebox.showinfo("Error", "Please select the\n\
Mothur executable file.")
        else:
            mothdir = Path(gfile).parent
            os.chdir(mothdir)
            os.system('cmd /k "mothur"')
    root2c = tkinter.Toplevel()
    root2c.title("Open MOTHUR")
    opnm_lbl = tkinter.Label(root2c, text = "\t\t\t\t\t\t\nPlease navigate to and select\n\
the Mothur executable file.\n").pack(anchor=CENTER)
    opnm_button = tkinter.Button(root2c, text='Select Mothur', command = selmothurexe).pack(anchor=CENTER)
    spacerm1_lbl = tkinter.Label(root2c, text = " ").pack(anchor=CENTER) #add space between buttons


#End MOTHUR program commands    
    

#Start R Commands

def runrinstr():
    def cont1():
        RWidgetWindow()
        rootr1.destroy()    
    rootr1 = tkinter.Toplevel()#makes window
    rootr1.title("Instructions")
    rootr1.geometry("300x140")
    instr1_lbl = tkinter.Label(rootr1, text = '\nPrior to running R, \
please ensure\nthat all required files and executables are\nin a single \
folder for ease of use.\n').pack(anchor=CENTER)#instructions
    cont1_button = tkinter.Button(rootr1, text='Continue', command = cont1).pack(anchor=CENTER)#continue to os used
    spacerm1_lbl = tkinter.Label(rootr1, text = " ").pack(anchor=CENTER) #add space between buttons


#Define a function to open a window widget to run R
def RWidgetWindow():
    top = Toplevel()
    top.title("R Hub")
    #Custom the dimention of the window
    top.geometry("300x300")
    lbl_1 = tkinter.Label(top, text = "\nPlease \
select from the following R options.\n").pack(anchor=CENTER)
    button1 = Button(top, text="Command Line", command= run_R_exe, width = 20).pack(anchor=CENTER)
    space1_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button2 = Button(top, text="Batch Mode", command= runBat, width = 20).pack(anchor=CENTER)
    space2_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button3 = Button(top, text="Phyloseq\nData Visualization", command= phylo_Widget, width = 20).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button4 = Button(top, text="Download Phyloseq", command= dldphylo, width = 20).pack(anchor=CENTER)
    space4_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button5 = Button(top, text="Close", command=top.destroy, width = 20).pack(anchor=CENTER)
    space4_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)


def selrdir():
    global dirrpath
    try:
        dirrpath = filedialog.askdirectory(title = 'Select the Directory to use')
    except:
        dirrpath = dirrpath
    if dirrpath == "":
        messagebox.showinfo("", "No directory selected.")


def selectrexe():
    global rpath
    rpath = ""
    try:
        rpath = filedialog.askopenfilename(title = 'Select the Rscript.exe', filetypes = ( ("\
Files", ("Rscript.exe")), ("All files", "*.*" ) ) )
    except:
        rpath = rpath
    if rpath == "":
        messagebox.showinfo("Note", "No file selected.")

def renameRplots():  
    def renameRplots2():
        global dirrpath
        newRplotsname = renameplotentry.get()
        if newRplotsname == "":
            newRplotsname2 = 'Rplots' + time.strftime("%Y%m%d-%H%M%S") + '.pdf'
            os.rename(dirrpath + '/' + 'Rplots.pdf', dirrpath + '/' + newRplotsname2)            
            answer = messagebox.askquestion(" ","Do you want to open the plots file (PDF)?")# Open plots PDF
            if answer == "yes":
                subprocess.Popen('"' + dirrpath + '/' + newRplotsname2 + '"', shell=True)

        else:
            os.rename(dirrpath + '/' + 'Rplots.pdf', dirrpath + '/' + newRplotsname + '.pdf')
            answer = messagebox.askquestion(" ","Do you want to open the plots file (PDF)?")# Open plots PDF
            if answer == "yes":
                subprocess.Popen('"' + dirrpath + '/' + newRplotsname + '.pdf"', shell=True)
        rootrename.destroy()

    global dirrpath
    rootrename = tkinter.Toplevel()
    rootrename.title('Rename Rplots.pdf')


    renameplot_lbl = tkinter.Label(rootrename, text = '\t\t\t\t\t\nPlease enter the filename for\n\
the plot file (e.g. plot1).\nIf none is entered, the default is\nRplots followed by a timestamp.\n').pack(anchor=CENTER)
    renameplotentry = tkinter.Entry(rootrename)
    renameplotentry.pack(anchor=CENTER)#label    
    spacerm1_lbl = tkinter.Label(rootrename, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(rootrename, text='Continue', command = renameRplots2).pack(anchor=CENTER)#classify.otu button.
    spacerm2_lbl = tkinter.Label(rootrename, text = " ").pack(anchor=CENTER) #add space
    
#Define a function to open R on window command line
def run_R_exe():    
    def choose_file():
        rootR.destroy()
        try: 
            f1= filedialog.askopenfile(title = 'Navigate the "R" folder in the MiSeq_SOP Directory until you get to the "R.exe" file in the "bin" folder',filetypes=[("Executable files", "*.exe")])# Open a file dialog to choose a file
            f2 = f1.name # Get the name of the file
            os.system('start cmd /k "' +'color 89 &&' + 'mode con: cols=80 lines=50 &&'+'title cmd (Running R Interactively)&& '+ f2)# Open a Windown command prompt and the R terminal
        except:
            messagebox.showinfo("Note", "No text file selected.")
    answer = messagebox.askquestion(" ","Do you really want to run R interactively?")# Ask the user if he wants to run R in the interactive mode
    if answer == "yes":
        rootR = tkinter.Toplevel()
        rootR.title("Select R.exe")
        rootR.geometry("500x125")
        label_R = tkinter.Label(rootR, text = '\nPlease navigate to and select \
the R executable file "R.exe" from the folder R.\n\
Note: If it does not exist, please make sure to have a copy of R in\n\
the folder containing the sequence files you wish to analyze.\n').pack(anchor=CENTER)
        button_R = tkinter.Button(rootR, text='Select Path for R', command = choose_file).pack(anchor=CENTER)#runs choose_file() to open R
##End run_R_exe()    
        

#Define a function to run R batch files
def runBat():
    def rb():
        selectrexe()
    def rd():
        selrdir()
    def rcom():
        try:
            rcommandsfile = filedialog.askopenfile(title = "Select the R or Text file to use", filetypes=[("All Files", "*.*")])
        except:
            rcommandsfile = ""
            messagebox.showinfo("Note", "No file selected.")
    def Run_Batch():
        global rpath
        global dirrpath
        global rcommandsfile
        if rpath == "":
            messagebox.showinfo("Note", "No Rscript.exe file selected.")
        elif dirrpath == "":
            messagebox.showinfo("Note", "No directory selected.")        
        else:
            if rcommandsfile == "":
                rcommandsfile = '"' + dirrpath + '/R_Command.txt"'
            newbatch = 'Rbatch' + time.strftime("%Y%m%d-%H%M%S") + '.bat'
            f = open(dirrpath + '/' + newbatch,'w+') #creates batch file
            f.write('"' + rpath + '"  "' + rcommandsfile + '"')
            f.close()
            os.chdir(dirrpath)
            os.system('cmd /k "' +'color 89 &&' + 'mode con: cols=80 lines=50 &&'+'title cmd (System Running an R Batch File)&& '+ newbatch)

    global rpath
    global dirrpath
    global rcommandsfile
     
    top = Toplevel()
    top.title("R Batch Mode")
    #Custom the dimention of the window
    top.geometry("500x400")
    Label1 = tkinter.Label(top, text = '\n\
Please navigate to and select both the location of the\n\
"Rscript.exe" file and the R or Text file containing the\n\
commands you wish to run.\n\
If no text file is selected, the batch file will use the\n\
text file "R_Commands.txt" which came with this version of\n\
 the MOTHUR GUI to be used as an example if needed.\n\
The batch files will be named "Rbatch" and append a timestamp.\n\
If you run the example, please check the "Rplots.pdf" file\n\
in your directory.\n').pack(anchor=CENTER)
    button1 = Button(top, text="Select Rscript.exe", command = rb, width = 20).pack(anchor= CENTER)
    lbl1 = tkinter.Label(top, text = ' ').pack(anchor=CENTER)
    button2 = Button(top, text="Select Directory", command = rd, width = 20).pack(anchor= CENTER)
    lbl1 = tkinter.Label(top, text = ' ').pack(anchor=CENTER)
    button3 = Button(top, text="Select Commands File", command = rcom, width = 20).pack(anchor= CENTER)
    lbl1 = tkinter.Label(top, text = ' ').pack(anchor=CENTER)
    button4 = Button(top, text="Continue", command = Run_Batch, width = 20).pack(anchor= CENTER)
    lbl1 = tkinter.Label(top, text = ' ').pack(anchor=CENTER)


#Define a widget with phyloseq functionalities
def phylo_Widget():
    def phyloExample(): #This function will execute phyloseq R script
        def cont(var):
            global dirrpath
            global rpath
            var = rad1.get()
            if var==1:
                selrdir()
                selectrexe()
                
                if dirrpath == "":
                    messagebox.showinfo("Note", "No directory selected.")
                elif rpath == "":
                    messagebox.showinfo("Note", "No Rscript.exe selected.")
                else:
                    tempphylo2 = 'plylo2' + time.strftime("%Y%m%d-%H%M%S") + '.R'
                    f2 = open(dirrpath + '/' + tempphylo2,'a+') #creates temporary mini text file
                    f2.write('library("phyloseq")'+'\n')
                    f2.write('library("ggplot2")'+'\n')
                    f2.write('theme_set(theme_bw())'+'\n')
                    f2.write('data(GlobalPatterns)'+'\n')
                    f2.write('GP <- prune_taxa(taxa_sums(GlobalPatterns) > 0, GlobalPatterns)'+'\n')
                    f2.write('human <- get_variable(GP, "SampleType") %in% c("Feces", "Mock", "Skin", "Tongue")'+'\n')
                    f2.write('sample_data(GP)$human <- factor(human)'+'\n')
                    f2.write('alpha_meas = c("Observed", "Chao1", "ACE", "Shannon", "Simpson", "InvSimpson")'+'\n')
                    f2.write('(p <- plot_richness(GP, "human", "SampleType", measures=alpha_meas))'+'\n')
                    f2.write('p + geom_boxplot(data=p$data, aes(x=human, y=value, color=NULL), alpha=0.1)'+'\n')
                    f2.write('GP.chl <- subset_taxa(GP, Phylum=="Chlamydiae")'+'\n')
                    f2.write('plot_tree(GP.chl, color="SampleType", shape="Family", label.tips="Genus", size="Abundance")'+'\n')
                    f2.close()

                    #Make a temporary batch file that runs a sample script for phyloseq
                    tempphylo1 = 'phylo1'+ '.bat'
                    f1 = open(dirrpath + '/' + tempphylo1,'w+') #creates mini batch file
                    f1.write('"' + rpath + '"  "' + tempphylo2 + '"')
                    f1.close()

                    os.chdir(dirrpath)
                    os.system('cmd /k "' + tempphylo1 + '"')# Open a Windown command prompt to run the batch file
                    os.remove(dirrpath + '/' + tempphylo1) #remove temp file
                    os.remove(dirrpath + '/' + tempphylo2) #remove temp file
                    renameRplots()

                    
                    

            if var==2:
                selrdir()
                selectrexe()
                
                if dirrpath == "":
                    messagebox.showinfo("Note", "No directory selected.")
                elif rpath == "":
                    messagebox.showinfo("Note", "No Rscript.exe selected.")
                else:
                
                    tempphylo3 = 'phylo3' + time.strftime("%Y%m%d-%H%M%S") + '.R'
                    f5 = open(dirrpath + '/' + tempphylo3,'a+') #creates mini batch file
                    f5.write('library("phyloseq")'+'\n')
                    f5.write('library("ggplot2")'+'\n')
                    f5.write('theme_set(theme_bw())'+'\n')
                    f5.write('data(enterotype)'+'\n')
                    f5.write('par(mar = c(10, 4, 4, 2) + 0.1) # make more room on bottom margin'+'\n')
                    f5.write('N <- 30'+'\n')
                    f5.write('rank_names(enterotype)'+'\n')
                    f5.write('TopNOTUs <- names(sort(taxa_sums(enterotype), TRUE)[1:10])'+'\n')
                    f5.write('ent10   <- prune_taxa(TopNOTUs, enterotype)'+'\n')
                    f5.write('print(ent10)'+'\n')
                    f5.write('sample_variables(ent10)'+'\n')
                    f5.write('plot_bar(ent10, "SeqTech", fill="Enterotype", facet_grid=~Genus)'+'\n')
                    f5.close()
                
                    #Make a temporary batch file that runs a sample script for phyloseq
                    tempphylo5 = 'phylo5'+ '.bat'
                    f6 = open(dirrpath + '/' + tempphylo5,'w+') #creates mini batch file
                    f6.write('"' + rpath + '"  "' + tempphylo3+ '"')
                    f6.close()

                    os.chdir(dirrpath)
                    os.system('cmd /k "' + tempphylo5 )
                    os.remove(dirrpath + '/' + tempphylo5) #remove temp file
                    os.remove(dirrpath + '/' + tempphylo3) #remove temp file
                    
            
        top = Toplevel()
        top.title("Run phyloseq examples")
        top.geometry("500x200")
        rad1 = tkinter.IntVar()
        rad1.set("0")
        label = tkinter.Label(top, text = '\nPlease, select an example from the buttons below\nand click the "Continue" button.', font=("ARIAL", 10 )).pack(anchor=CENTER) 
        rb1 = tkinter.Radiobutton(top, text=" This first example will output two plots and a tree."+"\n"+"Subject are humans and samples from feces, mock, skin,and tongue", variable=rad1, value=1).pack(anchor=W)
        rb2 = tkinter.Radiobutton(top, text="This second example shows the enterotype (Abundance per sequencing technonology)", variable=rad1, value=2).pack(anchor=W)
        cont_button = tkinter.Button(top, text='Continue', command = lambda: cont(rad1.get())).pack(anchor=CENTER)
        
    def phyloInfo():#Takes you to Bioconductor to see phyloseq package
        def Biofunction():
            webbrowser.open_new("https://bioconductor.org//packages//release//bioc//html//phyloseq.html")
            
        top1 = Toplevel()
        top1.title("Phyloseq Info")
        #Custom the dimention of the window
        top1.geometry("300x150")
        msglabel = tkinter.Label(top1, text = "You will be redirected to the Bioconductor website.\nPlease feel free to explore the phyloseq pipeline.\n").pack(anchor=CENTER)        
        button1 = Button(top1, text="Go to Bioconductor", width = 20, command= Biofunction).pack(anchor=CENTER)#Run Biofunction
        spacer = tkinter.Label(top1, text = " ").pack(anchor=CENTER)
        button2 = Button(top1, text="Close", width = 20, command=top1.destroy).pack(anchor=CENTER)

        
    def Rvisual():
        def rvisseldir():
            selrdir()
        def rvisselr():
            selectrexe()
        def ftypedisplay():
            selectglobalfile("list")
        def ftypedisplay2():
            selectglobalfile2("groups")
        def ftypedisplay3():
            selectglobalfile3("tree")
        def Rvisual2():
            global dirrpath
            global rpath
            global gfile
            global gfile2
            global gfile3

            list1 = [dirrpath, rpath, gfile, gfile2, gfile3]
            list2 = [' Directory ', ' Rscript.exe ', ' list file ', ' groups file ', ' tree file ']
            test = 0

            for i in range(len(list1)):
                if list1[i] == "":
                    test = 1
                    messagebox.showinfo("Note", "No" + list2[i] + "selected.")
                    break

            if test == 0:
                #Create a temporary txt file
                Tempofile = 'Tempofile' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
                f5 = open(dirrpath + '/' + Tempofile,'a+')
                #Append the script
                f5.write('library("phyloseq")'+'\n')
                f5.write('library("ggplot2")'+'\n')
                f5.write('library("vegan")'+'\n')
                f5.write('library("scales")'+'\n')
                f5.write('library("grid")'+'\n')
                f5.write('library("reshape2")'+'\n')
                f5.write('theme_set(theme_bw())'+'\n')
                f5.write('mothur_list_file  <-'+'"'+gfile+'"'+'\n')
                f5.write('mothur_group_file <-'+'"'+gfile2+'"'+'\n')
                f5.write('mothur_tree_file  <- '+'"'+gfile3+'"'+'\n')
                f5.write('show_mothur_cutoffs(mothur_list_file)'+'\n')
                f5.write('test1 <- import_mothur(mothur_list_file, mothur_group_file, mothur_tree_file)'+'\n')
                f5.write('test2 <- import_mothur(mothur_list_file, mothur_group_file, mothur_tree_file, cutoff="0.02")'+'\n')
                f5.write('test3 <- import_mothur(mothur_list_file, mothur_tree_file=mothur_tree_file)'+'\n')
                f5.write('plot(test3)'+'\n')
                f5.write('test4 <- import_mothur(mothur_list_file, mothur_group_file=mothur_group_file)'+'\n')
                f5.write('plot(test4)'+'\n')
                f5.close()
                
                #set the directory
                os.chdir(dirrpath)
                #Make a temporary batch file that runs a sample script for phyloseq
                tempbatch = 'R1'+ '.bat'
                f1 = open(dirrpath + '/' + tempbatch,'w+') #creates mini batch file
                f3 = f1.name
                f1.write('"' + rpath +'"  "'+os.path.basename(f5.name)+'\n'+'pause')
                f1.close()
                os.system('cmd /k "' +'title cmd (System Running an R Batch File)&& '+ tempbatch)
                os.remove(dirrpath + '/' + Tempofile) #remove temp file
                os.remove(dirrpath + '/' + tempbatch) #remove temp file
                renameRplots()
        global gfile
        global gfile2
        global gfile3
        gfile = ""
        gfile2 = ""
        gfile3 = ""
        rootrv = tkinter.Toplevel()
        rootrv.title('R Visual')
        ssfile1_lbl = tkinter.Label(rootrv, text = '\t\t\t\t\t\nPlease select the Directory to use\n\
and the Rscript.exe file as needed.\n').pack(anchor=CENTER)
        sf1_button = tkinter.Button(rootrv, text='Select Directory', command = rvisseldir).pack(anchor=CENTER)#Select the file button.
        spacerm2_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space between buttons
        ssf2_button = tkinter.Button(rootrv, text='Select Rscript.exe', command = rvisselr).pack(anchor=CENTER)#Select the file button.
        spacerm2_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space between buttons
        ssfile2_lbl = tkinter.Label(rootrv, text = '\t\t\t\t\t\nPlease select the list, groups,\n\
and tree files to use for\nvisualization, then click Continue.\n').pack(anchor=CENTER)
        ssf1_button = tkinter.Button(rootrv, text='Select List File', command = ftypedisplay).pack(anchor=CENTER)#Select the file button.
        spacerm2_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space between buttons
        ssf2_button = tkinter.Button(rootrv, text='Select Groups File', command = ftypedisplay2).pack(anchor=CENTER)#Select the file button.
        spacerm2_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space between buttons
        ssf3_button = tkinter.Button(rootrv, text='Select Tree File', command = ftypedisplay3).pack(anchor=CENTER)#Select the file button. 
        spacerm2_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space between buttons
        cont_button = tkinter.Button(rootrv, text='Continue', command = Rvisual2).pack(anchor=CENTER)#remove.lineage button.
        spacerm3_lbl = tkinter.Label(rootrv, text = " ").pack(anchor=CENTER) #add space        
    top = Toplevel()
    top.title("Data Visualization")#This widget allow the user to run the phyloseq package on R and see the output in the Rplots.pdf file
    #Custom the dimention of the window
    top.geometry("300x300")
    msg_lbl = tkinter.Label(top, text = "\nPlease select from the following options.\n").pack(anchor=CENTER)
    button1 = Button(top, text="phyloseq Interactive Mode", command= phylo_Interactive, width = 25).pack(anchor=CENTER)#Phyloseq is supported by 'R', so this button runs R interactively
    space1_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button2 = Button(top, text="phyloseq Examples", command= phyloExample, width = 25).pack(anchor=CENTER)
    space2_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button3 = Button(top, text="phyloseq Manual", command= phyloInfo, width = 25).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button4 = Button(top, text="Import from mothur\nand visualize", command= Rvisual, width = 25).pack(anchor=CENTER)
    space4_lbl = tkinter.Label(top, text = " ").pack(anchor=CENTER)
    button5 = Button(top, text="Close", command=top.destroy, width = 25).pack(anchor=CENTER)
##End phylo_Widget()
    


#Define a function to run phyloseq interactively. It means opening R on the command line
def phylo_Interactive():
    answer1 = messagebox.askquestion(" ","Do you really want to run phyloseq interactivelly ? \nBe advised that you will be redirected to R on the command line.")# Ask the user if he wants to run phyloseq in the interactive mode
    if answer1 == "yes":
        run_R_exe()



def dldphylo():
    def selr():
        selectrexe()

    def dldphylo2():
        global rpath
        global dirrpath
        if rpath == "":
            messagebox.showinfo("Error", "Please select Rscript.exe.")
        elif dirrpath == "":
            messagebox.showinfo("Error", "Please select a directory.")
        else:
            temprpath = dirrpath
            
            #Make two temp files with the timestamp for uniqueness
            tempRmakefile = 'tempRfile' + time.strftime("%Y%m%d-%H%M%S") + '.R'
            tempRbatchmakefile = 'tempRbatchfile' + time.strftime("%Y%m%d-%H%M%S") + '.bat'
            fr = open(temprpath + '/' + tempRmakefile,'w+') #creates mini batch file
            fr.write('if (!requireNamespace("BiocManager", quietly = TRUE)) \
install.packages("BiocManager")\n\n\
BiocManager::install("phyloseq")')
            fr.close()
            frbat = open(temprpath + '/' + tempRbatchmakefile,'w+') #creates mini batch file
            frbat.write('"' + rpath  + '" "' + temprpath + '/' + tempRmakefile + '"')
            frbat.close()
            #'cmd /c *terminate*, cmd /k *remain*
            os.chdir(temprpath) #set directory
            os.system('cmd /k "' + tempRbatchmakefile + '"') #run mini batch file
            os.remove(temprpath + '/' + tempRmakefile) #remove temp file
            os.remove(temprpath + '/' + tempRbatchmakefile) #remove temp file
            rootrd.destroy()
               
        
    global rpath
    global dirrpath
    dirrpath = ""
    rootrd = tkinter.Toplevel()
    rootrd.title('Download Phyloseq')
    mcfile_lbl = tkinter.Label(rootrd, text = '\t\t\t\t\t\nPlease navigate to and select the Rscript\n\
executable file and directory.\n').pack(anchor=CENTER)
    mcf1_button = tkinter.Button(rootrd, text='Select Rscript.exe', command = selr, width = 25).pack(anchor=CENTER)#Select the R.exe button.
    spacerm1_lbl = tkinter.Label(rootrd, text = " ").pack(anchor=CENTER) #add space between buttons
    mcf1_button = tkinter.Button(rootrd, text='Select Directory', command = selrdir, width = 25).pack(anchor=CENTER)#Select the R.exe button.
    spacerm1_lbl = tkinter.Label(rootrd, text = " ").pack(anchor=CENTER) #add space between buttons
    cont_button = tkinter.Button(rootrd, text='Continue', command = dldphylo2, width = 25).pack(anchor=CENTER)#make.contigs button.
    spacerm2_lbl = tkinter.Label(rootrd, text = " ").pack(anchor=CENTER) #add space

#END R Commands
    

#START Mothur Resources - Links to websites

def mothurresources():
    def dldmothur(): 
        webbrowser.open("https://www.mothur.org/")
    def mothurwiki():
        webbrowser.open("https://mothur.org/wiki/Main_Page")
    def miseqsop():
        webbrowser.open_new("https://www.mothur.org/wiki/MiSeq_SOP")
    def phyloseq():
        webbrowser.open_new("https://bioconductor.org/packages/release/bioc/html/phyloseq.html")
    rootmr = tkinter.Toplevel()
    rootmr.title("External Resources")
    rootmr.geometry("300x290")
    msg_lbl = tkinter.Label(rootmr, text = "\nPlease select from the following options.\n").pack(anchor=CENTER)
    # Create a widget button to open download MOTHUR link
    b = Button(rootmr, text = 'Download MOTHUR', command = dldmothur, width = 20).pack(anchor=CENTER)
    space1_lbl = tkinter.Label(rootmr, text = " ").pack(anchor=CENTER)
    # Create a widget button to open MOTHUR wiki link
    b2 = Button(rootmr, text = 'MOTHUR Wiki', command=mothurwiki, width = 20).pack(anchor=CENTER)
    space2_lbl = tkinter.Label(rootmr, text = " ").pack(anchor=CENTER)
    # Create a widget button to open MiSeq SOP link
    b3 = Button(rootmr, text = 'MiSeq SOP',command=miseqsop, width = 20).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(rootmr, text = " ").pack(anchor=CENTER)
    # Create a widget button to open MiSeq SOP link
    b4 = Button(rootmr, text = 'Phyloseq Info',command=phyloseq, width = 20).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(rootmr, text = " ").pack(anchor=CENTER)
    # Create a widget button to close window
    close = Button(rootmr, text = 'Close', command=rootmr.destroy, width = 20).pack(anchor=CENTER)
    space3_lbl = tkinter.Label(rootmr, text = " ").pack(anchor=CENTER)

#END Mothur Resources

#START Visualize Text File

#Define a function to read files
def openfile():
    try:
        file1 = filedialog.askopenfile()
        #label = Label(text=file1).pack()
        #Get the file name and store it in file1
        file2 = file1.name
        #Use a variable (file object) to open the file 
        f = open(file2, encoding='utf8', errors='ignore')

        top = Toplevel()
        top.title(file2)
	#Custom the dimention of the window
        top.geometry("1000x1000")
	#Create a scrollbar and indicate where it goes
        scrollbar = Scrollbar(top)
	#Pack the scrollbar to the widget
        scrollbar.pack( side = RIGHT, fill = Y )
	
	# Optional: Create a label with the content of the file and stick it to the window (top)
	#Optional:label2 = Label(top,text=f.read()).pack()

	#Create a text area
        textArea= Text(top, height = 100, width=100, wrap=WORD)
	# Insert the file content into the text area
        textArea.insert(END, f.read())
	#Cofigure the text area with font and size
        textArea.configure(font=("Courier", 10))
	#Attach the scrollbar to the text area
        scrollbar.config(command=textArea.yview)
	#Attach the text area to the scrollbar
        textArea.configure(yscrollcommand= scrollbar.set)
	#Pack the the text area
        textArea.pack()
    except:
        messagebox.showinfo("Note", "No text file selected.")
        
#END Visualize Text File


#START Biographies

#Definine a function for Authors'Biblio
def biblio():
    top1 = Toplevel()
    top1.title("Project Authors")
    #Custom the dimention of the window
    top1.geometry("275x150")
    member_lbl = tkinter.Label(top1, text = "\nList of Project Authors:\
\n\nConstant Nemi\nGuerlain Ulysse\nLauren Oglesby\nTaylor Shick\n\
Yazmin Ortiz-Mares").pack(anchor=CENTER)

        

        
#END Biographies

def main():
    mainmenu()
main()  


