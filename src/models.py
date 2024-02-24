import os
import sys
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    correo_electronico = Column(String(100), nullable=False)
    contraseña = Column(String(100), nullable=False) 
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(100), nullable=False)
    fecha_de_creacion = Column(DateTime, default=datetime.utcnow)
    posts = relationship("Post", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    contenido = Column(String(280), nullable=False)  
    fecha_de_publicacion = Column(DateTime, default=datetime.utcnow)
    usuario = relationship("Usuario", back_populates="posts")
    comentarios = relationship("Comentario", back_populates="post")

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    contenido = Column(String(280), nullable=False)
    fecha_de_comentario = Column(DateTime, default=datetime.utcnow)
    usuario = relationship("Usuario", back_populates="comentarios")
    post = relationship("Post", back_populates="comentarios")

class Seguidores(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario_seguido_id = Column(Integer, ForeignKey('usuario.id'))
    fecha_de_seguimiento = Column(DateTime, default=datetime.utcnow)
    usuario = relationship("Usuario", foreign_keys=[usuario_id])
    usuario_seguido = relationship("Usuario", foreign_keys=[usuario_seguido_id])

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
