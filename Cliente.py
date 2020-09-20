#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""
import sleekxmpp
import curses

class Cliente(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.mensajes='Nada'
        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start, threaded=True)
        self.add_event_handler("message", self.mensajeNuevo)
    
    def mensajeNuevo(self,msg):
        print(msg)
        self.mensajes='nuevo Mensaje'
    
    def getMensajePrueba(self):
        return self.mensajes
    
    def desconectarse(self):
        # Using wait=True ensures that the send queue will be
        # emptied before ending the session.
        print('Entra al metodo')
        self.disconnect()
        print('Cierra sesion')
    
    def eliminarCuenta(self,usuario,contra):
        self.registerPlugin('xep_0030')
        self.registerPlugin('xep_0077')
        self.plugin['xep_0077'].setForm('username', 'password')

    
    def enviarMensaje(self,contacto,mensaje):
        print('Enviar mensaje')
        self.sendMessage(mto=contacto,
                          mbody=mensaje,
                          mtype='chat')

    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        self.send_presence()
        self.get_roster()

