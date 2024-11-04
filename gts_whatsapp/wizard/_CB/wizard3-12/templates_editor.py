�
    �(gG  �                   �R   � d dl mZmZ ddlmZmZmZ  G d� dej                  �      Zy)�   )�Config�
get_reopen�    )�api�fields�modelsc                   ��   � e Zd ZdZd� Z ej                  eddd��      Z ej                  d��      Z	 e
j                  d	�      d
� �       Z e
j                  d�      d� �       Zd� Zy)�TemplatesEditorzgts_whatsapp.templates_editorc                 �   � d� }t        | �      j                  d�      j                  �       D �cg c]  }| ||�      f�� c}S c c}w )Nc                 �b   � | j                  dd�      j                  dd�      j                  �       S )Nzstock.action_report_� �_� )�replace�
capitalize)�template_ids    �wizard/templates_editor.py�<lambda>z8TemplatesEditor.get_template_selection.<locals>.<lambda>	   s-   � �{�':�':�;Q�SU�'V�'^�'^�_b�dg�'h�'s�'s�'u� �    �templates_text)r   �get�keys)�self�humanifyr   s      r   �get_template_selectionz&TemplatesEditor.get_template_selection   s>   � �u��HN�t��HX�HX�Yi�Hj�Ho�Ho�Hq�r���h�{�3�4�r�r��rs   �AzTemplate NameT�sales_quotations)�string�required�defaultzTemplate Text)r   �templatec                 �p   � | j                   r*t        | �      j                  | j                   �      | _        y y �N)r    r   �get_template_text�template_text�r   s    r   �onchange_templatez!TemplatesEditor.onchange_template   s)   � ��=�=�!'���!?�!?����!N�D�� r   r$   c                 �|   � | j                   r0t        | �      j                  | j                  | j                   �       y y r"   )r$   r   �set_template_textr    r%   s    r   �onchange_template_textz&TemplatesEditor.onchange_template_text   s.   � �����4�L�*�*�4�=�=�$�:L�:L�M� r   c                 �   � t        | �      j                  dd �       t        | �       t        | �      j                  | j                  �      | _        t        | d�      S )Nr   zWhatsapp Templates Editor)r   �setr#   r    r$   r   r%   s    r   �resetzTemplatesEditor.reset   sI   � ��t����)�4�0��t�� $�D�\�;�;�D�M�M�J����$� ;�<�<r   N)�__name__�
__module__�__qualname__�_namer   r   �	Selectionr    �Textr$   r   �onchanger&   r)   r,   � r   r   r
   r
      s   � �+�E�s�  �v��� 6��Y]�gy�z�H��F�K�K��7�M��S�\�\�*��O� �O� �S�\�\�/�"�N� #�N�	=r   r
   N)	�	global_pyr   r   �odoor   r   r   �TransientModelr
   r4   r   r   �<module>r8      s    �� *� $� $�=�f�+�+� =r   