from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from BE.Open import setting
from sqlalchemy.types import Unicode, UnicodeText, NVARCHAR

conn = setting().conectionsstr()
engine = create_engine(str(conn))
Base = declarative_base()


class low(Base):
    __tablename__ = "low"
    Id = Column(Integer, primary_key=True)
    FullName = Column(Unicode)
    PhoneNumber = Column(NVARCHAR)
    PersonId = Column(NVARCHAR)
    FullAddress = Column(Unicode)
    JobTitle = Column(Unicode)
    HowFindUs = Column(Unicode)
    FileType = Column(Unicode)
    CaseType = Column(NVARCHAR)
    PartyInLawsuit = Column(NVARCHAR)
    CaseStatues = Column(NVARCHAR)
    JudgmentIssued = Column(NVARCHAR)
    JudgmentPending = Column(NVARCHAR)
    History = Column(NVARCHAR)

    def __init__(self, FullName="", PhoneNumber="", PersonId="", FullAddress="", JobTitle="", HowFindUs="", FileType="",
                 CaseType="", PartyInLawsuit="", CaseStatues="", JudgmentIssued="", JudgmentPending="", History=""):
        self.FullName = FullName
        self.PhoneNumber = PhoneNumber
        self.PersonId = PersonId
        self.FullAddress = FullAddress
        self.JobTitle = JobTitle
        self.HowFindUs = HowFindUs
        self.FileType = FileType
        self.CaseType = CaseType
        self.PartyInLawsuit = PartyInLawsuit
        self.CaseStatues = CaseStatues
        self.JudgmentIssued = JudgmentIssued
        self.JudgmentPending = JudgmentPending
        self.History = History


class Appointment(Base):
    __tablename__ = "appointments"
    Id = Column(Integer, primary_key=True)
    ClientName = Column(NVARCHAR)
    AppointmentDate = Column(NVARCHAR)
    AppointmentTime = Column(NVARCHAR)
    Notes = Column(UnicodeText)

    def __init__(self, ClientName="", AppointmentDate="", AppointmentTime="", Notes=""):
        self.ClientName = ClientName
        self.AppointmentDate = AppointmentDate
        self.AppointmentTime = AppointmentTime
        self.Notes = Notes


class Safe(Base):
    __tablename__ = "Safe"
    Id = Column(Integer, primary_key=True)
    FullName = Column(NVARCHAR)
    UserName = Column(NVARCHAR)
    Password = Column(NVARCHAR)
    Role = Column(NVARCHAR)

    def __init__(self, FullName="", UserName="", Password="", Role=""):
        self.FullName = FullName
        self.UserName = UserName
        self.Password = Password
        self.Role = Role


Base.metadata.create_all(engine)
