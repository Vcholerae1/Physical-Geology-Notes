# 部署到服务器
import subprocess

def deploy(build_path, server_site_path, server):
    # 删除服务器站点路径下的所有文件
    subprocess.run(['ssh', server, f'rm -rf {server_site_path}/*'], check=True)
    # 上传并覆盖服务器上的文件
    subprocess.run(['scp', '-r', f'{build_path}/*', f'{server}:{server_site_path}'], check=True)
    # 设置 755 权限
    subprocess.run(['ssh', server, 'chmod', '-R', '755', server_site_path], check=True)
    # 重载 Caddy 服务器
    subprocess.run(['ssh', server, 'systemctl reload caddy'], check=True)

if __name__ == "__main__":
    # 本地构建路径
    build_path = './Physical-Geology/site'
    # 服务器站点路径
    server_site_path = '/var/www/geo'
    # 服务器地址
    server = 'clawcloud-hk'

    deploy(build_path, server_site_path, server)