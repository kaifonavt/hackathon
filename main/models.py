import enum
from typing import Union, List, Optional
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Table,
    Date,
    Time,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.mutable import MutableDict, MutableList
from database import Base

# Association tables
course_students = Table(
    "course_students",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("users.id"), index=True),
    Column("course_id", Integer, ForeignKey("courses.id"), index=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    avatar = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    total_points = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_activity = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    enrolled_courses = relationship("Course", secondary=course_students, back_populates="students")
    schedules = relationship("Schedule", back_populates="student")
    goals = relationship("PersonalGoal", back_populates="user")
    certificates = relationship("Certificate", back_populates="user")
    portfolio = relationship("Portfolio", uselist=False, back_populates="user")
    badges = relationship("UserBadge", back_populates="user")
    activity_logs = relationship("ActivityLog", back_populates="user")
    leaderboard_entry = relationship("LeaderboardEntry", uselist=False, back_populates="user")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    total_lessons = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    students = relationship("User", secondary=course_students, back_populates="enrolled_courses")
    lessons = relationship("Lesson", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")
    certificates = relationship("Certificate", back_populates="course")

class Schedule(Base):
    __tablename__ = "schedules"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    code = Column(String(10), nullable=False, index=True)  # A490, K190, etc.
    day_of_week = Column(Integer, nullable=False)  # 1-5 для Пн-Пт
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True)
    progress_percentage = Column(Float, default=0)
    completed_lessons = Column(Integer, default=0)
    enrollment_date = Column(DateTime(timezone=True), server_default=func.now())
    completion_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(MutableDict.as_mutable(JSON), default={"status": "active"})

    # Relationships
    course = relationship("Course", back_populates="enrollments")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    order = Column(Integer, nullable=False)
    points = Column(Integer, default=0)
    lesson_metadata = Column(MutableDict.as_mutable(JSON), default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    course = relationship("Course", back_populates="lessons")
    schedules = relationship("Schedule", back_populates="lesson")

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    number = Column(Integer, unique=True, index=True)
    styles = Column(MutableDict.as_mutable(JSON), default={})
    requirements = Column(MutableDict.as_mutable(JSON), default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user_badges = relationship("UserBadge", back_populates="badge")

class UserBadge(Base):
    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    badge_id = Column(Integer, ForeignKey("badges.id"), index=True)
    earned_date = Column(DateTime(timezone=True), server_default=func.now())
    userbadge_metadata = Column(MutableDict.as_mutable(JSON), default={})

    # Relationships
    user = relationship("User", back_populates="badges")
    badge = relationship("Badge", back_populates="user_badges")

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True)
    certificate_number = Column(String, unique=True, index=True)
    template_data = Column(MutableDict.as_mutable(JSON), default={})
    status = Column(String, default="active")
    issue_date = Column(DateTime(timezone=True), server_default=func.now())
    revocation_date = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    user = relationship("User", back_populates="certificates")
    course = relationship("Course", back_populates="certificates")

class PersonalGoal(Base):
    __tablename__ = "personal_goals"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    target_date = Column(Date, nullable=False)
    status = Column(String, default="pending")
    progress_data = Column(MutableDict.as_mutable(JSON), default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="goals")

class LeaderboardEntry(Base):
    __tablename__ = "leaderboard_entries"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True)
    points = Column(Integer, default=0)
    rank = Column(Integer, index=True)
    stats = Column(MutableDict.as_mutable(JSON), default={})
    last_calculated = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="leaderboard_entry")

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True)
    summary = Column(Text, nullable=True)
    skills = Column(MutableDict.as_mutable(JSON), default={})
    achievements_summary = Column(MutableDict.as_mutable(JSON), default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="portfolio")

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    activity_type = Column(String, nullable=False)
    description = Column(Text)
    points_earned = Column(Integer, default=0)
    activity_log_metadata = Column(MutableDict.as_mutable(JSON), default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="activity_logs")