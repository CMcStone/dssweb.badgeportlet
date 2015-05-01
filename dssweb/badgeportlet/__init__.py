from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles

PloneMessageFactory = MessageFactory('plone')

setDefaultRoles(
    'dssweb.badgeportlet: Add badge portlet',
    ('Manager', 'Site Administrator', 'Owner', )
)
