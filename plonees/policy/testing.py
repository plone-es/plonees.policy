from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class PloneesPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonees.policy
        xmlconfig.file('configure.zcml',
                       plonees.policy,
                       context=configurationContext
                   )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonees.policy:default')

PLONEES_POLICY_FIXTURE = PloneesPolicy()
PLONEES_POLICY_INTEGRATION_TESTING = IntegrationTesting(
        bases=(PLONEES_POLICY_FIXTURE,),
        name="Plonees:Integration"
    )
