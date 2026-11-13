from django.contrib.staticfiles import finders
from django.test import SimpleTestCase


class PageTests(SimpleTestCase):
    def test_homepage_renders_with_static_assets(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mateo Londoño Colorado')
        self.assertContains(response, '/static/css/tooplate-2169-hustle-bee.css')
        self.assertContains(response, '/static/js/tooplate-2169-hustle-bee.js')
        self.assertContains(response, '/static/img/images/design-work.jpg')
        self.assertContains(response, 'datos personales')
        self.assertContains(response, 'Estudios realizados')
        self.assertContains(response, 'Experiencia laboral')
        self.assertContains(response, 'class="project-card reveal"', count=2)
        self.assertContains(response, 'control de acceso y pagos de la unidad residencial Piemonte')
        self.assertContains(response, 'Calendario interactivo')
        self.assertContains(response, '/static/img/images/dashboard-project.jpg')
        self.assertContains(response, '/static/img/images/design-workspace.jpg')

    def test_timer_page_renders(self):
        response = self.client.get('/timer/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Timer')

    def test_static_assets_are_discoverable(self):
        for asset in (
            'css/tooplate-2169-hustle-bee.css',
            'js/tooplate-2169-hustle-bee.js',
            'img/images/design-work.jpg',
        ):
            with self.subTest(asset=asset):
                self.assertIsNotNone(finders.find(asset))
