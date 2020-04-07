


from github import Github
from templates import *

ACTOR_LABEL="acteur"
USECASE_DIR="UC"

def getcolor(label):
    if label=="actor" or label == ACTOR_LABEL :
            return "660066"
    if label=="UC" or label == USECASE_DIR:
            return "bada51"
    return "red"


class MyRepoException(Exception):
    pass


class MyRepo:
    def __init__(self,token,name):
        self.connection= Github(token)
        self.user = self.connection.get_user()
        

        self.link= "http://github.com/"+self.user.login+"/"+name+"/"
        self.basicrepo= self.connection.get_repo(self.user.login+"/"+name)
        self.project = self.basicrepo.get_projects(state="all")[0]
        self.createfile("UC/number",content="1")        
        
    def getrepo(self):
            return self.basicrepo

    def getproject(self):
        return self.project

    def createfile(self,filename, content="vide"):
        try:
            self.basicrepo.get_contents(filename)
            return False # file exist
        except Exception as x:
            if x.status ==404:
                self.basicrepo.create_file(filename,"message de creation ",content)
                return True
            else:
                raise x

    def getUcNumber(self, increment=False):
        c = self.basicrepo.get_contents(USECASE_DIR+"/number")
        current = int(c.decoded_content)
        if increment :
            b  = self.basicrepo.update_file(USECASE_DIR+"/number","incrementing "+str(current+1),str(current+1),c.sha)
            #print(b)
        return current

    
    def lastissuenumber(self):
        issues = self.basicrepo.get_issues()
        
        for i in issues :
            return i.number
        else:
            return 0
        
    def getLabel(self,label):
        for l in self.basicrepo.get_labels():
            if l.name==label :
                return [l]
        return [self.basicrepo.create_label(label,getcolor(label),description="Un des acteurs")]
    
    def createCardAndIssue(self,artefact, title, ):
        # FIXME
        pass
    
    def createIssue(self, title, corp, labels):
        issue= self.basicrepo.create_issue(title, body=corp,labels=labels)
        return issue 
        
    def createcard(self,name=" a card", link=" link to ressource",nbissue=0):        
        content=cardTemplate.render(name=name, link=link, nbissue=nbissue)
        return self.project.get_columns()[0].create_card(content)


    def addUseCase(self,actor,concept,usecasename,comment):
        """
        addUseCase(self,acteur,concept,usecasename)
        actor/$actor.md est créer avec template jinja ActeurTemplate
        une carte dans le projet ellaboration 
        et une issue -> editer l'acteur 
        puis 
        usecase/$actor/$usecaneme.md avec le template jinja UseCaseTemplate
        puis 
        un carte dans le projet
        et une issue  
        repo/ellaboration -> editer le cas d'utilisation 
        """
        d={}
        d['actor']=actor
        d['concept']=concept
        d['ucname']=usecasename

        d['comment']=comment
        
        actorfilename=ACTOR_LABEL+"/"+actor+".md"
        actorEdit= f"[Edition de {actor}]({self.link}edit/master/{actorfilename})"
        usecasefilename=USECASE_DIR+"/"+actor+"/"+usecasename+".md"
        ucEdit= f"[{usecasename}]({self.link}edit/master/{usecasefilename}) "
        
        
        if self.createfile(actorfilename, content= ActeurTemplate.render(actor=actor,concept=concept,usecase=usecasename)):
            # if it's a creation create the corresponding card
            issue = self.createIssue(f"[{ACTOR_LABEL}] {actor}",f"Edition de {actor} {actorEdit}", labels=self.getLabel(ACTOR_LABEL))
            
            d['nbissue']=issue.number
            self.createcard(actor+" card",actorfilename,issue.number)
            print("Création de l'acteur ", actor,)

        d['nbuc'] = self.getUcNumber(increment=False)
        if self.createfile(usecasefilename, content= usecaseTemplate.render(d)):
            d['nbuc'] = self.getUcNumber(increment=True)
            issueUC = self.createIssue(f"[{actor}]:{usecasename}",f" Le cas d'utilisation {ucEdit} \n étape: écriture", labels=self.getLabel(USECASE_DIR))
   
            self.createcard(actor+" card",usecasefilename,issueUC.number)
            print("Création du cas d'utilisation  ",usecasename)    
            
import sys

import csv 

def createPlantUmlFromCsv(filename="concept.csv", dirname="/home/dominique/projects/plansPlatons/UML/"):

    with open(filename,"r") as csvfile:
        reader=csv.DictReader(csvfile,delimiter=';')
        for row in reader:
				
def createUseCaseFromFile(repository, filename="concept.csv"):

    with open(filename,"r") as csvfile:
        reader=csv.DictReader(csvfile,delimiter=';')
        rows=[row for row in reader]
 
	actors=set() 
	UV=set() 
	actorUc= defaultdict(list)
	for row in rows:
		actors.add(row['actor'])
		us.add(row['UC'])
		actorUc[row['actor']].append(row['UC'])

	for a,l in actorUc.items():
		with open(a+".du","w") as f :
			print("@startuml",file=f)
			print("actor "+a,file=f)
			for uc in l:
				print(f"({uc})",file=f)
			print("@enduml",file=f)
	
# or using an access token
# g = Github("eaea9e96d448a187bed89c7ad3578711f20a7640")

# createUseCaseFromFile(MyRepo("eaea9e96d448a187bed89c7ad3578711f20a7640","cards"))

sys.exit()
