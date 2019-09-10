# import unittest
# import random
# from django.test import Client
#
# from SayaraApi.models import RefVersion, Image, RefModele, Fabricant, RefCouleur, RefOption, LigneTarif, FicheTechnique
# from SayaraApi.models import Vehicule, Marque, Version, Modele, Annonce, Profile, Couleur, Option
#
#
# def create_image(**kwargs):
#     defaults = {}
#     defaults["image"] = "image"
#     defaults.update(**kwargs)
#     return Image.objects.create(**defaults)
#
#
# def create_vehicule(**kwargs):
#     defaults = {}
#     defaults["num"] = "num"
#     defaults["vehicule"] = "vehicule"
#     defaults.update(**kwargs)
#     return Vehicule.objects.create(**defaults)
#
#
# def create_marque(**kwargs):
#     defaults = {}
#     defaults["nom"] = "nom" + str(RefVersion.objects.count() + 1)
#     defaults["image"] = "image"
#     defaults.update(**kwargs)
#     return Marque.objects.create(**defaults)
#
#
# def create_refversion(**kwargs):
#     defaults = {}
#     size = RefVersion.objects.all()
#     defaults["nom"] = "nom" + str(RefVersion.objects.count() + 1)
#
#     defaults.update(**kwargs)
#     return RefVersion.objects.create(**defaults)
#
#
# def create_version(**kwargs):
#     defaults = {}
#     defaults["code"] = "code"
#     defaults["prix_base"] = "prix_base"
#     defaults.update(**kwargs)
#     if "nom" not in defaults:
#         defaults["nom"] = create_refversion()
#     if "images" not in defaults:
#         defaults["images"] = create_image()
#     if "options" not in defaults:
#         defaults["options"] = create_option()
#     if "modele" not in defaults:
#         defaults["modele"] = create_modele()
#     if "ficheTechnique" not in defaults:
#         defaults["ficheTechnique"] = create_fichetechnique()
#     if "couleur" not in defaults:
#         defaults["couleur"] = create_couleur()
#     return Version.objects.create(**defaults)
#
#
# def create_refmodele(**kwargs):
#     defaults = {}
#     defaults["nom"] = "nom" + str(RefModele.objects.count() + 2)
#     defaults.update(**kwargs)
#     if "marque" not in defaults:
#         defaults["marque"] = create_marque()
#     return RefModele.objects.create(**defaults)
#
#
# def create_modele(**kwargs):
#     defaults = {}
#     defaults["code"] = "code"
#     defaults["image"] = "image"
#     defaults.update(**kwargs)
#     if "nom" not in defaults:
#         defaults["ref"] = create_refmodele()
#     return Modele.objects.create(**defaults)
#
#
# def create_annonce(**kwargs):
#     defaults = {}
#     defaults["titre"] = "titre"
#     defaults["prix"] = "prix"
#     defaults["commentaires"] = "commentaires"
#     defaults.update(**kwargs)
#     if "vehicule" not in defaults:
#         defaults["vehicule"] = create_vehiculeoccasion()
#     if "user" not in defaults:
#         defaults["user"] = create_user()
#     return Annonce.objects.create(**defaults)
#
#
# def create_fabricant(**kwargs):
#     defaults = {}
#     defaults["nom"] = "nom"
#     defaults.update(**kwargs)
#     return Fabricant.objects.create(**defaults)
#
#
# def create_profile(**kwargs):
#     defaults = {}
#     defaults["is_fabricant"] = "is_fabricant"
#     defaults["is_client"] = "is_client"
#     defaults.update(**kwargs)
#     if "fabricant" not in defaults:
#         defaults["fabricant"] = create_fabricant()
#     return Profile.objects.create(**defaults)
#
#
# def create_refcouleur(**kwargs):
#     defaults = {}
#     defaults["nom"] = "nom" + str(RefCouleur.objects.count() + 1)
#     defaults.update(**kwargs)
#     return RefCouleur.objects.create(**defaults)
#
#
# def create_couleur(**kwargs):
#     defaults = {}
#     defaults["code"] = "code"
#     defaults.update(**kwargs)
#     if "nom" not in defaults:
#         defaults["ref"] = create_refcouleur()
#     if "modele" not in defaults:
#         defaults["modele"] = create_modele()
#     return Couleur.objects.create(**defaults)
#
#
# def create_refoption(**kwargs):
#     defaults = {}
#     defaults["nom"] = "nom" + str(RefOption.objects.count() + 1)
#     defaults.update(**kwargs)
#     return RefOption.objects.create(**defaults)
#
#
# def create_option(**kwargs):
#     defaults = {}
#     defaults["code"] = "code"+str(Option.objects.count()+1)
#     defaults["ref"] = create_refoption()
#     defaults["modele"] = create_modele()
#     return Option.objects.create(**defaults)
#
#
# def create_lignetarif(**kwargs):
#     defaults = {}
#     defaults["dateDebut"] = "dateDebut"
#     defaults["dateFin"] = "dateFin"
#     defaults["prix"] = "prix"
#     defaults.update(**kwargs)
#     return LigneTarif.objects.create(**defaults)
#
#
# def create_fichetechnique(**kwargs):
#     defaults = {}
#     defaults["nombrePortes"] = 10
#     defaults["boiteVitesse"] = "boiteVitesse"
#     defaults["puissanceFiscale"] = "puissanceFiscale"
#     defaults["motorisation"] = "motorisation"
#     defaults["consommation"] = "consommation"
#     defaults["dimensions"] = "dimensions"
#     defaults["transmission"] = "transmission"
#     defaults["capaciteReservoir"] = "capaciteReservoir"
#     defaults["vitesseMaxi"] = 100
#     defaults["acceleration"] = "acceleration"
#     defaults.update(**kwargs)
#     return FicheTechnique.objects.create(**defaults)
#
#
# class MarqueViewTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_list_marque(self):
#         url = str('/api/marque/')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_create_marque(self):
#         url = str('/api/marque/create/')
#         data = {
#             "nom": "nom",
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 201)
#
#     def test_detail_marque(self):
#         marque = create_marque()
#         url = '/api/marque/detail/' + str(marque.pk) + '/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_marque(self):
#         marque = create_marque()
#         data = {
#             'pk': marque.pk,
#             "nom": "nosm2",
#         }
#         url = '/api/marque/update/' + str(marque.pk) + '/'
#         response = self.client.put(url, data, content_type="application/json")
#         self.assertEqual(response.status_code, 200)
#
#
# class VersionViewTest(unittest.TestCase):
#     '''
#     Tests for Version
#     '''
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_list_version(self):
#         url = str('/api/version/')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_create_version(self):
#         url = str('/api/version/create/')
#         data = {
#             "code": "code",
#             "prix_base": "prix_base",
#             "ref": create_refversion().pk,
#             "images": create_image().pk,
#             "options": create_option().pk,
#             "modele": create_modele().pk,
#             "ficheTechnique": create_fichetechnique().pk,
#             "couleur": create_couleur().pk,
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 302)
#
#     def test_detail_version(self):
#         version = create_version()
#         url = '/api/version/detail/' + str(version.pk) + '/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_version(self):
#         version = create_version()
#         data = {
#             "nomVersion": "nomVersion",
#             "codeVersion": "codeVersion",
#         }
#         url = '/api/version/update/' + str(version.pk) + '/'
#         response = self.client.put(url, data, content_type="application/json")
#         self.assertEqual(response.status_code, 302)
#
#
# #
# # class ModeleViewTest(unittest.TestCase):
# #     '''
# #     Tests for Modele
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_modele(self):
# #         url = str('/api/modele/')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_modele(self):
# #         url = str('/api/modele/create/')
# #         data = {
# #             "idModele": "idModele",
# #             "nomModele": "nomModele",
# #             "couleurCompatible": create_couleur().pk,
# #             "marqueModele": create_marque().pk,
# #             "couleurCompatible": create_couleur().pk,
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_modele(self):
# #         modele = create_modele()
# #         url = '/api/modele/detail/' + str(modele.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_modele(self):
# #         modele = create_modele()
# #         data = {
# #             "idModele": "idModele",
# #             "nomModele": "nomModele",
# #             "couleurCompatible": create_couleur().pk,
# #             "marqueModele": create_marque().pk,
# #             "couleurCompatible": create_couleur().pk,
# #         }
# #         url = '/api/modele/update/' + str(modele.pk) + '/'
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, 302)
# #
# #
# # class AnnonceViewTest(unittest.TestCase):
# #     '''
# #     Tests for Annonce
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_annonce(self):
# #         url = str('/api/annonce/')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     # def test_create_annonce(self):
# #     #     url = str('/api/annonce/create/')
# #     #     data = {
# #     #         "titre": "titre",
# #     #         "prix": "prix",
# #     #         "commentaites": "commentaites",
# #     #     }
# #     #     response = self.client.post(url, data=data)
# #     #     self.assertEqual(response.status_code, 302)
# #     #
# #     # def test_detail_annonce(self):
# #     #     annonce = create_annonce()
# #     #     url = '/api/annonce/detail/' + str(annonce.pk) + '/'
# #     #     response = self.client.get(url)
# #     #     self.assertEqual(response.status_code, 200)
# #     #
# #     # def test_update_annonce(self):
# #     #     annonce = create_annonce()
# #     #     data = {
# #     #         "titre": "titre",
# #     #         "prix": "prix",
# #     #         "commentaites": "commentaites",
# #     #     }
# #     #     url = '/api/annonce/update/' + str(annonce.pk) + '/'
# #     #     response = self.client.post(url, data)
# #     #     self.assertEqual(response.status_code, 302)
#
#
# # class FabricantViewTest(unittest.TestCase):
# #     '''
# #     Tests for Fabricant
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_Fabricant(self):
# #         url = str('/api/fabricant/')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_Fabricant(self):
# #         url = str('/api/fabricant/create/')
# #         data = {
# #             "nomFabricant": "nomFabricant",
# #             "idFabricant": "idFabricant",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_Fabricant(self):
# #         Fabricant = create_Fabricant()
# #         url = '/api/fabricant/detail/' + str(Fabricant.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_Fabricant(self):
# #         Fabricant = create_Fabricant()
# #         data = {
# #             "nomFabricant": "nomFabricant",
# #             "idFabricant": "idFabricant",
# #         }
# #         url = '/api/fabricant/update/' + str(Fabricant.pk) + '/'
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, 302)
# #
# #
# # class CouleurViewTest(unittest.TestCase):
# #     '''
# #     Tests for Couleur
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_couleur(self):
# #         url = str('/api/couleur/')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_couleur(self):
# #         url = str('/api/couleur/create/')
# #         data = {
# #             "codeCouleur": "codeCouleur",
# #             "nomCouleur": "nomCouleur",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_couleur(self):
# #         couleur = create_couleur()
# #         url = '/api/couleur/detail/' + str(couleur.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_couleur(self):
# #         couleur = create_couleur()
# #         data = {
# #             "codeCouleur": "codeCouleur",
# #             "nomCouleur": "nomCouleur",
# #         }
# #         url = '/api/couleur/update/' + str(couleur.pk) + '/'
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, 302)
# #
# #
# # class OptionViewTest(unittest.TestCase):
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_option(self):
# #         url = str('/api/option/')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_option(self):
# #         url = str('/api/option/create/')
# #         data = {
# #             "nomOption": "nomOption",
# #             "codeOption": "codeOption",
# #             "kilometrage": "kilometrage",
# #             "date": "date",
# #             "disponible": "disponible",
# #             "idFabricant": create_Fabricant().pk,
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_option(self):
# #         option = create_option()
# #         url = '/api/option/detail/' + str(option.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_option(self):
# #         option = create_option()
# #         data = {
# #             "nomOption": "nomOption",
# #             "codeOption": "codeOption",
# #             "kilometrage": "kilometrage",
# #             "date": "date",
# #             "disponible": "disponible",
# #             "idFabricant": create_Fabricant().pk,
# #         }
# #         url = '/api/option/update/' + str(option.pk) + '/'
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, 302)
# #
# #
# # class RefVersionViewTest(unittest.TestCase):
# #     '''
# #     Tests for RefVersion
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_refversion(self):
# #         url = 'api/refversion/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_refversion(self):
# #         url = 'api/refversion/create/'
# #         data = {
# #             "nom": "nom"
# #
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
#
# def test_detail_refversion(self):
#     refversion = create_refversion()
#     url = 'api/refversion/detail/' + str(refversion.pk) + '/'
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)
#
#
# def test_update_refversion(self):
#     refversion = create_refversion()
#     data = {
#         "nom": "nom",
#     }
#     url = 'api/refversion/update/' + str(refversion.pk) + '/'
#     response = self.client.post(url, data)
#     self.assertEqual(response.status_code, 302)
#
# # class ImageViewTest(unittest.TestCase):
# #     '''
# #     Tests for Image
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_image(self):
# #         url = '/api/image/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_image(self):
# #         url = '/api/image/create/'
# #         data = {
# #             "image": "image",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_image(self):
# #         image = create_image()
# #         url = '/api/image/detail/' + str(image.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_image(self):
# #         image = create_image()
# #         data = {
# #             "image": "image",
# #         }
# #         url = '/api/image/update/' + str(image.pk) + '/'
# #         response = self.client.post(url, data,content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
# #
# # class RefModeleViewTest(unittest.TestCase):
# #     '''
# #     Tests for RefModele
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_refmodele(self):
# #         url = '/api/refmodele/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_refmodele(self):
# #         url = '/api/refmodele/create/'
# #         data = {
# #             "nom": "nom",
# #             "marque": create_marque().pk,
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_refmodele(self):
# #         refmodele = create_refmodele()
# #         url = '/api/refmodele/detail/' + str(refmodele.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_refmodele(self):
# #         refmodele = create_refmodele()
# #         data = {
# #             "nom": "nom",
# #             "marque": create_marque().pk,
# #         }
# #         url = '/api/refmodele/update/' + str(refmodele.pk) + '/'
# #         response = self.client.put(url, data,content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
#
# # class FabricantViewTest(unittest.TestCase):
# #     '''
# #     Tests for Fabricant
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_Fabricant(self):
# #         url = '/api/fabricant/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_Fabricant(self):
# #         url = '/api/fabricant/create/'
# #         data = {
# #             "nom": "nom",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_Fabricant(self):
# #         Fabricant = create_Fabricant()
# #         url = '/api/fabricant/detail/' + str(Fabricant.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_Fabricant(self):
# #         Fabricant = create_Fabricant()
# #         data = {
# #             "nom": "nom",
# #         }
# #         url = '/api/fabricant/update/' + str(Fabricant.pk) + '/'
# #         response = self.client.put(url, data, content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
# #
# # class RefCouleurViewTest(unittest.TestCase):
# #     '''
# #     Tests for RefCouleur
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_refcouleur(self):
# #         url = '/api/refcouleur/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_refcouleur(self):
# #         url = '/api/refcouleur/create/'
# #         data = {
# #             "nom": "nom",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_refcouleur(self):
# #         refcouleur = create_refcouleur()
# #         url = '/api/refcouleur/detail/' + str(refcouleur.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_refcouleur(self):
# #         refcouleur = create_refcouleur()
# #         data = {
# #             "nom": "nom",
# #         }
# #         url = '/api/refcouleur/update/' + str(refcouleur.pk) + '/'
# #         response = self.client.put(url, data, content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
# #
# # class RefOptionViewTest(unittest.TestCase):
# #     '''
# #     Tests for RefOption
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_refoption(self):
# #         url = '/api/refoption/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_refoption(self):
# #         url = '/api/refoption/create/'
# #         data = {
# #             "nom": "nom",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_refoption(self):
# #         refoption = create_refoption()
# #         url = '/api/refoption/detail/' + str(refoption.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_refoption(self):
# #         refoption = create_refoption()
# #         data = {
# #             "nom": "nom",
# #         }
# #         url = '/api/refoption/update/' + str(refoption.pk) + '/'
# #         response = self.client.put(url, data, content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
#
# # class LigneTarifViewTest(unittest.TestCase):
# #     '''
# #     Tests for LigneTarif
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_lignetarif(self):
# #         url = '/api/lignetarif/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_lignetarif(self):
# #         url = '/api/lignetarif/create/'
# #         data = {
# #             "dateDebut": "dateDebut",
# #             "dateFin": "dateFin",
# #             "prix": "prix",
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_lignetarif(self):
# #         lignetarif = create_lignetarif()
# #         url = '/api/lignetarif/detail/' + str(lignetarif.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_lignetarif(self):
# #         lignetarif = create_lignetarif()
# #         data = {
# #             "dateDebut": "dateDebut",
# #             "dateFin": "dateFin",
# #             "prix": "prix",
# #         }
# #         url = '/api/lignetarif/update/' + str(lignetarif.pk) + '/'
# #         response = self.client.put(url, data, content_type="application/json")
# #         self.assertEqual(response.status_code, 200)
# #
# #
# # class FicheTechniqueViewTest(unittest.TestCase):
# #     '''
# #     Tests for FicheTechnique
# #     '''
# #
# #     def setUp(self):
# #         self.client = Client()
# #
# #     def test_list_fichetechnique(self):
# #         url = '/api/fichetechnique/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_create_fichetechnique(self):
# #         url = '/api/fichetechnique/create/'
# #         data = {
# #             "nombrePortes": "nombrePortes",
# #             "boiteVitesse": "boiteVitesse",
# #             "puissanceFiscale": "puissanceFiscale",
# #             "motorisation": "motorisation",
# #             "consommation": "consommation",
# #             "dimensions": "dimensions",
# #             "transmission": "transmission",
# #             "capaciteReservoir": "capaciteReservoir",
# #             "vitesseMaxi": "vitesseMaxi",
# #             "acceleration": "acceleration",
# #             "images": create_image().pk,
# #         }
# #         response = self.client.post(url, data=data)
# #         self.assertEqual(response.status_code, 302)
# #
# #     def test_detail_fichetechnique(self):
# #         fichetechnique = create_fichetechnique()
# #         url = '/api/fichetechnique/detail/' + str(fichetechnique.pk) + '/'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_update_fichetechnique(self):
# #         fichetechnique = create_fichetechnique()
# #         data = {
# #             "nombrePortes": "nombrePortes",
# #             "boiteVitesse": "boiteVitesse",
# #             "puissanceFiscale": "puissanceFiscale",
# #             "motorisation": "motorisation",
# #             "consommation": "consommation",
# #             "dimensions": "dimensions",
# #             "transmission": "transmission",
# #             "capaciteReservoir": "capaciteReservoir",
# #             "vitesseMaxi": "vitesseMaxi",
# #             "acceleration": "acceleration",
# #             "images": create_image().pk,
# #         }
# #         url = '/api/fichetechnique/update/' + str(fichetechnique.pk) + '/'
# #         response = self.client.put(url, data, content_type="application/json")
# #         self.assertEqual(response.status_code, 302)
