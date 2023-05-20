"""add foreign-key to posts table

Revision ID: 450b5bbe8c16
Revises: ce988e1f7e8e
Create Date: 2023-05-19 14:35:24.964169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450b5bbe8c16'
down_revision = 'ce988e1f7e8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table= 'posts', referent_table= "users",
                          local_cols= ['owner_id'], remote_cols= ['id'], ondelete= "CASCADE")

    pass


def downgrade():
    op.drop_constraint('posts_users_fk', 'posts')
    op.drop_column('posts', 'owner_id')
    pass
