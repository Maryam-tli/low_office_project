from sqlalchemy import create_engine,Column,Integer,String,Text
from sqlalchemy.orm import declarative_base,sessionmaker
from BE.Open import setting

conn=setting().conectionsstr()
engine=create_engine(str(conn))
Base=declarative_base()
dade=sessionmaker(bind=engine)
session=dade()

class Repository():
    def Add(self,obj):
        session.add(obj)
        session.commit()
        return True

    def AddRegister(self,obj):
        session.add(obj)
        session.commit()
        return True

    def Read(self,tablename):
        return session.query(tablename).all()

    def Readbyid(self,tablename,id):
        m=session.query(tablename).filter(tablename.Id==id).first()
        return m

    def Update(self,tablename,id,**kwargs):
        s=self.Readbyid(tablename,id)
        for key,val in kwargs.items():
            setattr(s,key,val)
        session.commit()
        return True

    def Delete(self,tablename,id):
        r=session.query(tablename).filter(tablename.Id==id).first()
        session.delete(r)
        session.commit()
        return True

    def Search(self, TableName, search):
        result = session.query(TableName).filter((TableName.Id.like(f"%{search}%")) |
                                                 (TableName.FullName.like(f"%{search}%")) |
                                                 (TableName.PhoneNumber.like(f"%{search}%")) |
                                                 (TableName.PersonId.like(f"%{search}%")) |
                                                 (TableName.FullAddress.like(f"%{search}%")) |
                                                 (TableName.JobTitle.like(f"%{search}%")) |
                                                 (TableName.HowFindUs.like(f"%{search}%"))|
                                                 (TableName.FileType.like(f"%{search}%")) |
                                                 (TableName.CaseType.like(f"%{search}%")) |
                                                 (TableName.PartyInLawsuit.like(f"%{search}%")) |
                                                 (TableName.CaseStatues.like(f"%{search}%")) |
                                                 (TableName.JudgmentIssued.like(f"%{search}%")) |
                                                 (TableName.JudgmentPending.like(f"%{search}%")) |
                                                 (TableName.History.like(f"%{search}%")))
        result.all()
        return result


    def Searchappoint(self, TableName, search):
        result = session.query(TableName).filter((TableName.Id.like(f"%{search}%")) |
                                                 (TableName.ClientName.like(f"%{search}%")) |
                                                 (TableName.AppointmentDate.like(f"%{search}%")) |
                                                 (TableName.AppointmentTime.like(f"%{search}%")) |
                                                 (TableName.Notes.like(f"%{search}%")))
        result.all()
        return result

    def search_member(self, tablename, search):
        result = session.query(tablename).filter(
            (tablename.Id.like(f"%{search}%")) |
            (tablename.FullName.like(f"%{search}%")) |
            (tablename.UserName.like(f"%{search}%")) |
            (tablename.Password.like(f"%{search}%")) |
            (tablename.Role.like(f"%{search}%"))
        )
        return result.all()  # برای دریافت لیست کامل از نتایج

    def search_member_by_id(self, tablename, member_id):
        # بررسی صحت ورودی
        if not member_id:
            return None

        try:
            result = session.query(tablename).filter(tablename.Id == member_id).first()
            return result
        except Exception as e:
            print(f"Error in search_member_by_id: {e}")
            return None

    def vasl(self,tablename,newobj):
            l=session.query(tablename).filter((tablename.UserName==newobj.UserName) & (tablename.Password==newobj.Password)).first()
            if l==None:
                return False
            else:
                return l
