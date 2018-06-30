import numpy as np
from random import randrange
import requests
import language_check
from owlready2 import *
from .models import *
import os
import string
import ontospy
import pronto
from pronto import Term, Relationship
# from ontobio.ontol_factory import OntologyFactory

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class OntoCreate:
    def OntologyAddTerms(self):

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ont = pronto.Ontology(target)

        t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        t2 = Term('ONT:002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})
        ont.include(t1, t2)

        print(ont.obo)
        print("********************************* The Json Obj **************************************")
        print(ont.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)

    def AddSoftwareEngineerTerms(self):

        print("********************************* Adding SoftwareEngineer Terms to the ontology **************************************")

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ontSoftwareEngineer = pronto.Ontology(target)

        # t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        # t2 = Term('ONT:0002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})

        #region Here we prepare key value dataset to enter to the ontology
        #START
        termList = {}
        termList['Software engineering'] = 'Software engineering is an engineering branch associated with software system development'
        termList['Computer software'] = 'Computer software is a complete package, which includes software program, its documentation and user guide on how to use the software'
        termList['computer program'] = 'A computer program is piece of programming code which performs a well defined task'
        termList['Software Development Life Cycle(SDLC)'] = 'Software Development Life Cycle, or software process is the systematic development of software by following every stage in the development process namely, Requirement Gathering, System Analysis, Design, Coding, Testing, Maintenance and Documentation in that order'
        termList['Software project management'] = 'Software project management is process of managing all activities like time, cost and quality management involved in software development'
        termList['software project manager'] = 'A software project manager is a person who undertakes the responsibility of carrying out the software project'
        termList['Software scope'] = 'Software scope is a well-defined boundary, which encompasses all the activities that are done to develop and deliver the software product. The software scope clearly defines all functionalities and artifacts to be delivered as a part of the software. The scope identifies what the product will do and what it will not do, what the end product will contain and what it will not contain'
        termList['Baseline'] = 'Baseline is a measurement that defines completeness of a phase. After all activities associated with a particular phase are accomplished, the phase is complete and acts as a baseline for next phase'
        termList['Software Configuration management'] = 'Software Configuration management is a process of tracking and controlling the changes in software in terms of the requirements, design, functions and development of the product'
        termList['measure project execution'] = 'We can measure project execution by means of Activity Monitoring, Status Reports and Milestone Checklists'
        termList['feasibility study'] = {}
        termList['feasibility study']['feasibility study'] = 'It is a measure to assess how practical and beneficial the software project development will be for an organization. The software analyzer conducts a thorough study to understand economic, technical and operational feasibility of the project'
        termList['feasibility study']['Economic'] = 'Resource transportation, cost for training, cost of additional utilities and tools and overall estimation of costs and benefits of the project'
        termList['feasibility study']['Technical'] = 'Checking whether Is it possible to develop this system ? Assessing suitability of machine(s) and operating system(s) on which software will execute, existing developers’ knowledge and skills, training, utilities or tools for project'
        termList['feasibility study']['Operational'] = 'Checking whether Can the organization adjust smoothly to the changes done as per the demand of project ? Is the problem worth solving ?'
        termList['gather requirements'] = 'Requirements can be gathered from users via interviews, surveys, task analysis, brainstorming, domain analysis, prototyping, studying existing usable version of software, and by observation'
        termList['SRS or Software Requirement Specification'] = 'SRS or Software Requirement Specification is a document produced at the time of requirement gathering process. It can be also seen as a process of refining requirements and documenting them'
        termList['functional requirements'] = ' Functional requirements are functional features and specifications expected by users from the proposed software product'
        termList['non-functional requirements'] = 'Non-functional requirements are implicit and are related to security, performance, look and feel of user interface, interoperability, cost etc'
        termList['concurrency'] = 'Concurrency is the tendency of events or actions to happen simultaneously. In software, when two or more processes execute simultaneously, they are called concurrent processes'
        termList['cohesion'] = 'Cohesion is a measure that defines the degree of intra-dependability among the elements of the module'
        termList['Coupling '] = 'Coupling is a measure that defines the level of inter-dependability among modules of a program'
        termList['Data dictionary'] = 'Data dictionary is referred to as meta-data. Meaning, it is a repository of data about data. Data dictionary is used to organize the names and their references used in system such as objects and files along with their naming conventions'
        termList['Structured design'] = 'Structured design is a conceptualization of problem into several well-organized elements of solution. It is concern with the solution design and based on ‘divide and conquer’ strategy'
        termList['top-down and bottom-up design model'] = 'Top-down model starts with generalized view of system and decomposes it to more specific ones, whereas bottom-up model starts with most specific and basic components first and keeps composing the components to get higher level of abstraction'
        termList['functional programming'] = 'Functional programming is style of programming language, which uses the concepts of mathematical function. It provides means of computation as mathematical functions, which produces results irrespective of program state'
        termList['acid properties'] = {}
        termList['acid properties']['acid properties'] = 'ACID is an acronym for atomicity, consistency, isolation, and durability'
        termList['acid properties']['Atomicity'] = 'This property states that a transaction must be treated as an atomic unit, that is, either all of its operations are executed or none. There must be no state in a database where a transaction is left partially completed. States should be defined either before the execution of the transaction or after the execution/abortion/failure of the transaction'
        termList['acid properties']['Consistency '] = 'The database must remain in a consistent state after any transaction. No transaction should have any adverse effect on the data residing in the database. If the database was in a consistent state before the execution of a transaction, it must remain consistent after the execution of the transaction as well'
        termList['acid properties']['Durability '] = 'The database should be durable enough to hold all its latest updates even if the system fails or restarts. If a transaction updates a chunk of data in a database and commits, then the database will hold the modified data. If a transaction commits but the system fails before the data could be written on to the disk, then that data will be updated once the system springs back into action'
        termList['acid properties']['Isolation '] = 'In a database system where more than one transaction are being executed simultaneously and in parallel, the property of isolation states that all the transactions will be carried out and executed as if it is the only transaction in the system. No transaction will affect the existence of any other transaction'
        termList['JVM'] = 'JVM is an acronym for Java Virtual Machine, it is an abstract machine which provides the runtime environment in which java bytecode can be executed. It is a specification. JVMs are available for many hardware and software platforms (so JVM is platform dependent)'
        termList['JRE'] = 'JRE stands for Java Runtime Environment. It is the implementation of JVM'
        termList['JDK'] = 'JDK is an acronym for Java Development Kit. It physically exists. It contains JRE + development tools'
        termList['Just-In-Time(JIT) compiler'] = 'It is used to improve the performance. JIT compiles parts of the byte code that have similar functionality at the same time, and hence reduces the amount of time needed for compilation.Here the term “compiler” refers to a translator from the instruction set of a Java virtual machine (JVM) to the instruction set of a specific CPU'
        termList['platform'] = 'A platform is basically the hardware or software environment in which a program runs. There are two types of platforms software-based and hardware-based. Java provides software-based platform'
        termList['classloader'] = 'The classloader is a subsystem of JVM that is used to load classes and interfaces.There are many types of classloaders e.g. Bootstrap classloader, Extension classloader, System classloader, Plugin classloader etc'
        termList['difference between object oriented programming language and object based programming language'] = 'Object based programming languages follow all the features of OOPs except Inheritance. Examples of object based programming languages are JavaScript, VBScript etc'
        termList['constructor'] = 'Constructor is just like a method that is used to initialize the state of an object. It is invoked at the time of object creation'
        #END
        #endregion

        #region Here we add above prepared key value pairs to the ontology
        #START
        x =0
        termListObject = {}
        for key in termList:
            if(isinstance(key, str)):
                if(str(termList[key]).find("{")==-1): #not found { mark in termList[key]
                    x = x + 1
                    ontVal = 'ONT:' + str(x).zfill(6)
                    termListObject[ontVal] = Term('ONT:' + str(x).zfill(6), key, termList[key])

                else:
                    check = 1
                    for innerKey in termList[key]:
                        if (str(termList[key][innerKey]).find("{") == -1):
                            if (isinstance(innerKey, str)):
                                if(check==1):
                                    x = x + 1
                                    ontValInnerFirst = 'ONT:' + str(x).zfill(6)
                                    termListObject[ontValInnerFirst] = Term('ONT:' + str(x).zfill(6), innerKey, termList[key][innerKey])
                                    check= check + 1
                                else:
                                    x = x + 1
                                    ontValInner = 'ONT:' + str(x).zfill(6)
                                    termListObject[ontValInner] = Term('ONT:' + str(x).zfill(6), innerKey, termList[key][innerKey], {Relationship('part_of'): [ontValInnerFirst]})
                                    ontValToFollowNext = 'ONT:' + str(x + 1).zfill(6)
                        else:
                            for innerInnerKey in termList[key][innerKey]:
                                x = x + 1
                                ontValInnerInner = 'ONT:' + str(x).zfill(6)
                                termListObject[ontValInnerInner] = Term('ONT:' + str(x).zfill(6), innerInnerKey, termList[key][innerKey][innerInnerKey], {Relationship('part_of'): [ontValToFollowNext]})

        #END
        #endregion

        #region Here we add terms to the ontology using pronto include term
        #START
        for key in termListObject:
            ontSoftwareEngineer.include(termListObject[key])  #ontSoftwareEngineer.include(t1, t2)
        #END
        #endregion

        print(ontSoftwareEngineer.obo)
        print("********************************* The Json Obj **************************************")
        print(ontSoftwareEngineer.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)

        return ontSoftwareEngineer

    def AddQualityAsuranceEngineerTerms(self):

        print("********************************* Adding SoftwareEngineer Terms to the ontology **************************************")

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ontQualityAsuranceEngineer = pronto.Ontology(target)

        t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        t2 = Term('ONT:002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})
        ontQualityAsuranceEngineer.include(t1, t2)

        print(ontQualityAsuranceEngineer.obo)
        print("********************************* The Json Obj **************************************")
        print(ontQualityAsuranceEngineer.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)

    def AddBusinessAnalistTerms(self):

        print(
            "********************************* Adding SoftwareEngineer Terms to the ontology **************************************")

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ontBusinessAnalyst = pronto.Ontology(target)

        t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        t2 = Term('ONT:002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})
        ontBusinessAnalyst.include(t1, t2)

        print(ontBusinessAnalyst.obo)
        print("********************************* The Json Obj **************************************")
        print(ontBusinessAnalyst.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)

    def AddSystemEngineerTerms(self):

        print(
            "********************************* Adding SoftwareEngineer Terms to the ontology **************************************")

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ontSysystemEngineer = pronto.Ontology(target)

        t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        t2 = Term('ONT:002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})
        ontSysystemEngineer.include(t1, t2)

        print(ontSysystemEngineer.obo)
        print("********************************* The Json Obj **************************************")
        print(ontSysystemEngineer.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)

    def AddNetworkEngineerTerms(self):

        print(
            "********************************* Adding SoftwareEngineer Terms to the ontology **************************************")

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCVTest.owl"])

        ontNetworkEngineer = pronto.Ontology(target)

        t1 = Term('ONT:001', 'my 1st term', 'this is my first term')
        t2 = Term('ONT:002', 'my 2nd term', 'this is my second term', {Relationship('part_of'): ['ONT:001']})
        ontNetworkEngineer.include(t1, t2)

        print(ontNetworkEngineer.obo)
        print("********************************* The Json Obj **************************************")
        print(ontNetworkEngineer.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)