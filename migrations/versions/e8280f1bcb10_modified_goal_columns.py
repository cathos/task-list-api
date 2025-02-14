"""modified goal columns

Revision ID: e8280f1bcb10
Revises: 8a6cc2fcd4f0
Create Date: 2022-05-12 11:59:19.897549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8280f1bcb10'
down_revision = '8a6cc2fcd4f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
