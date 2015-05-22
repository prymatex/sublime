#!/usr/bin/env python

LISTENERS = []

class EventListenerMeta(type):
    def __new__(meta, name, bases, dct):
        super_new = super(EventListenerMeta, meta).__new__

        # Also ensure initialization is only performed for subclasses of EventListenerMeta
        # (excluding EventListenerMeta class itself).
        parents = [b for b in bases if isinstance(b, EventListenerMeta)]
        if not parents:
            return super_new(meta, name, bases, dct)
            
        new_class = super_new(meta, name, bases, dct)
        LISTENERS.append(new_class)
        return new_class

class EventListener(metaclass=EventListenerMeta):
    def on_activated(self, view):
        pass

    def on_deactivated(self, view):
        pass

    def on_pre_save(self, view):
        pass

    def on_post_save(self, view):
        pass
        
    def on_close(self, view):
        pass

    def on_modified(self, view):
        pass

    def on_selection_modified(self, view):
        pass

    def on_query_completions(self, view, prefix, locations):
        """locations son puntos en el documento"""
        pass
