# -*- coding: utf-8 -*-
import unittest2 as unittest
from plonees.policy.testing import PLONEES_POLICY_INTEGRATION_TESTING

from Products.PloneLanguageTool import LanguageTool
from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):

    layer = PLONEES_POLICY_INTEGRATION_TESTING

    # Testing Site Properties
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual(
                "Plone.es",
                portal.getProperty('title')
            )

    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual(
                "Bienvenido a Plone.es",
                portal.getProperty('description')
            )

    # Testing Language Settings
    def test_language_settings(self):
        portal = self.layer['portal']
        id = LanguageTool.id
        ltool = portal._getOb(id)
        defaultLanguage = 'es'
        self.failUnless(
                ltool.getDefaultLanguage()==defaultLanguage
            )
        supportedLanguages = ['es']
        self.failUnless(
                ltool.getSupportedLanguages()==supportedLanguages
            )
