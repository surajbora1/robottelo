"""Unit tests for the ``subscription`` paths.

A full API reference for subscriptions can be found here:
https://<sat6.com>/apidoc/v2/subscriptions.html

"""
from robottelo import entities
from unittest import TestCase
from robottelo.common.manifests import clone


class SubscriptionsTestCase(TestCase):
    """Tests for the ``subscriptions`` path."""

    def test_positive_create_1(self):
        """@Test: Upload a manifest.

        @Assert: Manifest is uploaded successfully

        @Feature: Subscriptions

        """
        cloned_manifest_path = clone()
        org_id = entities.Organization().create()['id']
        task_id = entities.Organization(id=org_id).upload_manifest(
            path=cloned_manifest_path
        )
        task_result = entities.ForemanTask(id=task_id).poll()['result']
        self.assertEqual(u'success', task_result)

    def test_positive_delete_1(self):
        """@Test: Delete an Uploaded manifest.

        @Assert: Manifest is Deleted successfully

        @Feature: Subscriptions

        """
        cloned_manifest_path = clone()
        org_id = entities.Organization().create()['id']
        task_id = entities.Organization(id=org_id).upload_manifest(
            path=cloned_manifest_path
        )
        task_result = entities.ForemanTask(id=task_id).poll()['result']
        self.assertEqual(u'success', task_result)
        task_id = entities.Organization(id=org_id).delete_manifest()
        task_result = entities.ForemanTask(id=task_id).poll()['result']
        self.assertEqual(u'success', task_result)

    def test_negative_create_1(self):
        """@Test: Upload same manifest to 2 different Organizations.

        @Assert: Manifest is not uploaded in the second Organization.

        @Feature: Subscriptions

        """
        cloned_manifest_path = clone()
        orgid_one = entities.Organization().create()['id']
        orgid_two = entities.Organization().create()['id']
        taskid_one = entities.Organization(id=orgid_one).upload_manifest(
            path=cloned_manifest_path
        )
        task_result = entities.ForemanTask(id=taskid_one).poll()['result']
        self.assertEqual(u'success', task_result)
        taskid_two = entities.Organization(id=orgid_two).upload_manifest(
            path=cloned_manifest_path
        )
        task_result = entities.ForemanTask(id=taskid_two).poll()['result']
        self.assertNotEqual(u'success', task_result)
