�
    
�(g�	  �                   �p   � d dl mZmZmZ d dlmZ ddlmZmZm	Z	m
Z
mZmZmZ  G d� dej        �  �        ZdS )�    )�api�fields�models)�ValidationError�   )�Config�	get_order�get_from_id�	fill_text�get_filextension�get_default_connection�remove_filextensionc                   ��   � � e Zd ZdZdZdgZ ej        dedd��  �        Z	 ej
        dd	d�
�  �        Z ej        d��  �        Z ej        d��  �        Zej        � fd��   �         Zd� Zdd�Zd� Z� xZS )�MessageMenuz whatsapp_contacts.messaging_menuzMessaging Menuzmail.threadzwhatsapp.connection�
ConnectionT)�default�string�required�res.partner�
Recipients)r   r   �Message)r   zDocument Namec                 �  �� t          t          | �  �        �                    |�  �        }d| j        j        v rI| j        j        d         }| j        d         �                    dd|fgd��  �        }|rdd|j        gfg|d	<   d
| j        j        v rJt          | �  �        �                    | j        j        d
         �  �        |d<   | j        j        d         |d<   |S )N�send_tor   �phone�=�   )�limit�   r   �
recipients�template_name�message�document_name)	�superr   �default_get�env�context�search�idr   �get_template_text)�selfr   �resr   �partner�	__class__s        ��wizard/message_menu.pyr$   zMessageMenu.default_get   s�   �� ��K��&�&�2�2�6�:�:�����(�(�(��H�$�Y�/�E��h�}�-�4�4�w��U�6K�5L�TU�4�V�V�G�� ;�&'��W�Z�L�%9�$:��L�!��d�h�.�.�.�#�D�\�\�;�;�D�H�<L�_�<]�^�^�C�	�N�#'�8�#3�O�#D�C�� ��
�    c                 �   � | j         �                    |�  �        }|�                    |t          | �  �        j        ��  �        \  }}|S )N)�res_ids)r%   �ref�_render_qweb_pdfr	   r(   )r*   �name�report�pdf_data�_s        r.   �generate_pdfzMessageMenu.generate_pdf#   s?   � �����d�#�#���-�-�d�I�d�O�O�<N�-�O�O���!��r/   Nc                 �$   � |�| j         S |d         S )Nr"   )r"   )r*   r+   s     r.   �get_document_namezMessageMenu.get_document_name)   s   � ��;��%�%���'�'r/   c                 ��  � | �                     �   �          | j        r'| �                    | �                    �   �         �  �        }t	          | | j        �  �        }t          | �  �        }|�                    d|� ���  �         | j        D ]j}| j        r:| j	        �
                    |j        ||| j        j        d         d         ��  �         �C| j        r | j	        �                    |j        |�  �         �kd S )NzWhatsapp message sent: )�body�	variablesz(slip-reference))�caption�filename)�
ensure_oner"   r8   r:   r   r!   r	   �message_postr   �
connection�send_pdfr   r%   r&   �send_message)r*   �pdf�text�order�	recipients        r.   rD   zMessageMenu.send_message0   s  � ��������� 	>��#�#�D�$:�$:�$<�$<�=�=�C���t�|�,�,���$������� @�$� @� @��A�A�A��� 	D� 	D�I��!� D���(�(���#�t�VZ�V^�Vf�gr�Vs�  uG�  WH�(�  I�  I�  I�  I��� D���,�,�Y�_�d�C�C�C��		D� 	Dr/   )N)�__name__�
__module__�__qualname__�_name�_description�_inheritr   �Many2oner   rB   �	Many2manyr   �Textr!   �Charr"   r   �modelr$   r8   r:   rD   �__classcell__)r-   s   @r.   r   r      s�   �� � � � � �.�E�#�L���H� ���!6�@V�_k�vz�{�{�{�J�!��!�-��t�T�T�T�J��f�k��+�+�+�G�  �F�K��7�7�7�M��Y�� � � � �Y�� � � �(� (� (� (�D� D� D� D� D� D� Dr/   r   N)�odoor   r   r   �odoo.exceptionsr   �	global_pyr   r	   r
   r   r   r   r   �TransientModelr   � r/   r.   �<module>rZ      s�   �� $� $� $� $� $� $� $� $� $� $� +� +� +� +� +� +� A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�  A�:D� :D� :D� :D� :D�&�'� :D� :D� :D� :D� :Dr/   