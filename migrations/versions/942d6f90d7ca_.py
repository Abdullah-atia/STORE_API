"""empty message

Revision ID: 942d6f90d7ca
Revises: 
Create Date: 2024-07-30 17:53:27.717498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942d6f90d7ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        op.execute("UPDATE invoices SET enable_downloads = False")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
