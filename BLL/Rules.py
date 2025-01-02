from DAL.Repository import Repository
from tkinter import messagebox

class Blrepository():
    def Add(self, obj):
        repos = Repository()
        repos.Add(obj)
        return True

    def AddRegister(self,obj):
        if obj.FileType == "Criminal Cases":
            # نمایش پیام هشدار
            messagebox.showerror("Error", "We do not accept criminal cases")
            return False
        if obj.FileType == "پرونده کیفری":
            messagebox.showerror("خطا", "پرونده‌های کیفری پذیرفته نمی‌شود.")
            return False

        else:
            repos = Repository()
            repos.AddRegister(obj)
            return True

    def Read(self, tablename):
        repos = Repository()
        return repos.Read(tablename)

    def Readbyid(self, tablename,id):
        repos = Repository()
        m=repos.Readbyid(tablename,id)
        return m

    def Update(self, tablename, id, **kwargs):
        repos = Repository()
        d=repos.Update(tablename,id,**kwargs)
        return d

    def Delete(self, tablename,id):
        repos = Repository()
        d=repos.Delete(tablename,id)
        return d


    def Search(self, tablename, search):
        repos = Repository()
        results = repos.Search(tablename, search)
        return results

    def Searchappoint(self,tablename,search):
        repos=Repository()
        results= repos.Searchappoint(tablename,search)
        return results

    def search_member(self,tablename,search):
        repos=Repository()
        results=repos.search_member(tablename,search)
        return results

    def search_member_by_id(self, tablename, member_id):
        repos=Repository()
        results=repos.search_member_by_id(tablename,member_id)
        return results

    def vasl(self,tablename,newobj):
        repos=Repository()
        res=repos.vasl(tablename,newobj)
        return res
