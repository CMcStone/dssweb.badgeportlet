from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = "dssweb.badgeportlet"
DEFAULT_ADD_CONTENT_PERMISSION = "%s: Add badge portlet" % PROJECTNAME

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION,
                ('Manager', 'Site Administrator', 'Owner',))