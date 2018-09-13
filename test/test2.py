import yaml
from docker_registry_client import DockerRegistryClient
import logging
import subprocess




class ChartsUtil:

    def __init__(self, new_charts_image):
        self._app_manager_file_path = "/opt/kubernetes/kubeaddons/transwarp-app-manager.yaml.complete"
        self._new_charts_image = new_charts_image

    def replace_charts_image(self):
        if not self._check_image():
            return
        try:
            subprocess.run(['cp', '-n', self._app_manager_file_path, "./transwarp-app-manager.yaml.complete.backup"])
            f = open(self._app_manager_file_path)
            app_manager_yaml = yaml.load(f)
            f.close()
            old_charts_image = app_manager_yaml['spec']['template']['spec']['initContainers'][0]['image']

            if old_charts_image == self._new_charts_image:
                logger.info("No change for charts image")
                return

            app_manager_yaml['spec']['template']['spec']['initContainers'][0]['image'] = self._new_charts_image
            logger.info(app_manager_yaml)

            f = open(self._app_manager_file_path, 'w+')
            yaml.dump(app_manager_yaml, f, default_flow_style=False)
            f.close()

            subprocess.run(['kubectl', '-n', 'kube-system', 'delete', 'deploy', 'app-manager'])
            subprocess.run(['kubectl', '-n', 'kube-system', 'apply', '-f', self._app_manager_file_path])

            logger.info('Image {} has been successfully applied in app-manager'.format(self._new_charts_image))

        except Exception as e:
            logger.info("Image replace failed: {}", self._new_charts_image)

    def _check_image(self):
        if self._new_charts_image is None:
            return False

        address = self._new_charts_image.split("/")

        if len(address) != 3:
            logger.error("The format of the image %s can not be converted" % self._new_charts_image)
            return False

        try:
            ip, namespace, repository, tag = address[0], address[1], address[2].split(":")[0], address[2].split(":")[1]
        except Exception as e:
            logger.error("The format of the image %s can not be converted" % self._new_charts_image)
            return False

        try:
            client = DockerRegistryClient("https://" + ip, verify_ssl=False)
            charts_repo = client.repository(repository, namespace)
            charts_tags = charts_repo.tags()
            if tag in charts_tags:
                logger.info("Find image: " + self._new_charts_image)
                return True
            else:
                logger.error("Could not find image: " + self._new_charts_image)
                return False
        except Exception as e:
            logger.error("Image query failed: {}".format(self._new_charts_image))
            return False

logger = logging.getLogger(__name__)
charts = ChartsUtil("172.16.3.234:5000/transwarp/transwarp_charts:tdc-1.1.0-rc1")
charts.replace_charts_image()