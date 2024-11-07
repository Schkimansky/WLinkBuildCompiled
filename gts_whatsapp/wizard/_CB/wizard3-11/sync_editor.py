�
    @�,g�  �                   �   � d dl mZmZmZ d dlmZ ddlmZmZm	Z	  G d� dej
        �  �        Z G d� dej        �  �        Zd	S )
�    )�api�fields�models)�ValidationError�   )�get_default_connection�	get_phone�
get_reopenc                   �   � e Zd ZdZdZ ej        dd��  �        Z ej        dd��  �        Z ej        dd��  �        Z	 ej
        ddd	�
�  �        ZdS )�Contact�gts_whatsapp.contactz Contact for gts_whatsapp.contact�PhoneT��string�required�Name�Username�KeepF)r   r   �defaultN)�__name__�
__module__�__qualname__�_name�_descriptionr   �Char�phone�name�username�Boolean�keep� �    �wizard/sync_editor.pyr   r      sr   � � � � � �"�E�5�L��F�K�w��6�6�6�E��6�;�f�t�4�4�4�D��v�{�*�t�<�<�<�H��6�>��$��F�F�F�D�D�Dr"   r   c                   ��   � e Zd ZdZdZ ej        dedd��  �        Z ej	        ddd�	�  �        Z
d
eeeeef                  fd�Z ej        d�  �        d� �   �         Zd� Zddedefd�Zd� Zd� Zd� ZdS )�
SyncEditorzgts_whatsapp.sync_editorz'SyncEditor for gts_whatsapp.sync_editorzwhatsapp.connectionzWhatsapp ConnectionT)r   r   r   r   zContacts to syncr   �datac                 �  � g }g }t          |�  �        D ]D\  }\  }}}d}|}	|dk    rd}t          |�  �        dz   |z   }	|�                    |	||||f�  �         �E|�                    d� ��  �         |D ]G\  }
}}}}| j        d         �                    ||||d��  �        }|�                    |j        �  �         �Hd	d
|fg| _        d S )NT�*Invalid name*F�   c                 �   � | d         S )Nr   r!   )�xs    r#   �<lambda>z+SyncEditor.setup_contacts.<locals>.<lambda>'   s
   � �q��t� r"   )�keyr   )r   r   r   r    �   r   )�	enumerate�len�append�sort�env�create�id�contacts_to_sync)�selfr&   �contact_ids�sorted_data�indexr   r   r   r    �sorter�_�contacts               r#   �setup_contactszSyncEditor.setup_contacts   s   � ����� /8��o�o� 	F� 	F�*�E�*�E�8�T��D��F��'�'�'����T���Q���.�������x��t�D�E�E�E�E� 	���^�^��,�,�,� /:� 	+� 	+�*�A�u�h��d��h�5�6�=�=��W[�iq�{�  ?A�  ?A�  B�  B�G����w�z�*�*�*�*�"#�Q��!4� 5����r"   �
connectionc                 �Z  � | j         r�| j         �                    t          �  �        }g }|D ]h}t          |d         �  �        }|�                    dd�  �        }|�                    dd�  �        }|dk    r|dk    r�P|�                    |||f�  �         �i| �                    |�  �         d S d S )Nr5   r   z*Invalid username*�pushnamer(   )r?   �get_contactsr   r	   �getr1   r>   )r7   �contactsr&   r=   r   r   r   s          r#   �reload_datazSyncEditor.reload_data0   s�   � ��?� 	&���3�3�O�D�D�H� 02�D�#� 7� 7��!�'�$�-�0�0��"�;�;�v�/C�D�D���{�{�:�/?�@�@���+�+�+��<P�0P�0P�����U�H�d�3�6�6�6�6�����%�%�%�%�%�	&� 	&r"   c                 �   � | j         D ]7}|j        r.| j        d         �                    |j        |j        dd��  �         �8d S )Nzres.partnerF)r   r   �
is_company)r6   r    r3   r4   r   r   )r7   r=   s     r#   �synchronizezSyncEditor.synchronizeC   s[   � ��,� 	x� 	x�G��|� x����'�.�.��8H�SZ�S`�pu�/v�/v�w�w�w��	x� 	xr"   Fr    �reloadc                 �   � | j         D ]0}t          |t          �   �         t          �   �         �  �        |_        �1|r| �                    �   �          t          | d�  �        S )NzWhatsapp Synchronization)r6   �eval�globals�localsr    rE   r
   )r7   r    rI   �records       r#   �base_selectzSyncEditor.base_selectI   sY   � ��+� 	:� 	:�F��t�W�Y�Y����9�9�F�K�K��%�4�#�#�%�%�%��$� :�;�;�;r"   c                 �,   � | �                     d�  �        S )N�True�rO   �r7   s    r#   �
select_allzSyncEditor.select_allQ   s   � ��!1�!1�&�!9�!9�9r"   c                 �,   � | �                     d�  �        S )N�FalserR   rS   s    r#   �deselect_allzSyncEditor.deselect_allR   s   � �4�#3�#3�G�#<�#<�<r"   c                 �,   � | �                     d�  �        S )Nzrecord.name == "*Invalid name*"rR   rS   s    r#   �select_saved_contactsz SyncEditor.select_saved_contactsS   s   � �D�,<�,<�=^�,_�,_�%_r"   N)F)r   r   r   r   r   r   �Many2oner   r?   �	Many2manyr6   �list�tuple�strr>   r   �onchangerE   rH   �boolrO   rT   rW   rY   r!   r"   r#   r%   r%      s  � � � � � �&�E�<�L� ���!6�@V�_t�  @D�  E�  E�  E�J�'�v�'�(>�GY�dh�i�i�i��6�4��c�3��m�(<�#=� 6� 6� 6� 6�2 �S�\�,���&� &�  ��&�$x� x� x�<� <�� <�T� <� <� <� <� :�9�9�<�<�<�_�_�_�_�_r"   r%   N)�odoor   r   r   �odoo.exceptionsr   �	global_pyr   r	   r
   �TransientModelr   �Modelr%   r!   r"   r#   �<module>rf      s�   �� $� $� $� $� $� $� $� $� $� $� +� +� +� +� +� +� E� E� E� E� E� E� E� E� E� E�G� G� G� G� G�f�#� G� G� G�C`� C`� C`� C`� C`��� C`� C`� C`� C`� C`r"   