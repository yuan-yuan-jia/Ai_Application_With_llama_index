"""
此模块构建整个应用程序中用到的各种索引
"""
from llama_index.core import (StorageContext, VectorStoreIndex, TreeIndex,load_index_from_storage)
from llama_index.core.indices.base import BaseIndex
from PITS.global_settings import INDEXS_STORAGE
def buil_indexes(nodes) -> tuple[BaseIndex,BaseIndex]:
    try:
        storage_context = StorageContext.from_defaults(persist_dir=str(INDEXS_STORAGE))
        vector_index = load_index_from_storage(storage_context=storage_context,index_id='vector')
        tree_index = load_index_from_storage(storage_context=storage_context,index_id='tree')
        print('All indices loaded from storage.')
    except Exception as e:
        print(f"Error occurred while loading indices: {e}")
        storage_context = StorageContext.from_defaults()
        vector_index = VectorStoreIndex(
            nodes,storage_context=storage_context
        )
        vector_index.set_index_id('vector')
        tree_index = TreeIndex(
            nodes,storage_context=storage_context
        )
        tree_index.set_index_id('tree')

        storage_context.persist(persist_dir=INDEXS_STORAGE)
        print('New indexes created and persisted.')
    return (vector_index,tree_index)