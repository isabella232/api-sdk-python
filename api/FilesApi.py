from smartlingApiSdk.ApiV2 import ApiV2

class FilesApi(ApiV2):

    def __init__(self, userIdentifier, userSecret, projectId, proxySettings=None, permanentHeaders={}, env='prod'):
        ApiV2.__init__(self, userIdentifier, userSecret, projectId, proxySettings, permanentHeaders=permanentHeaders, env=env)

    def uploadSourceFile(self, file, fileUri, fileType, authorize=False, localeIdsToAuthorize=[], callbackUrl='', directives={}, **kwargs):
        '''
            method  :  POST
            api url :  /files-api/v2/projects/{projectId}/file
            details :  https://api-reference.smartling.com/#operation/uploadSourceFile
            as curl :  curl -X POST -H "Authorization: Bearer $smartlingToken" -F "file=@$uploadFilePath;type=text/plain" -F "fileUri=$uploadFileSmartlingUri" -F "fileType=$uploadFileSmartlingType" "https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file"
        '''
        kw = {
            'file':self.processFile(file),
            'fileUri':fileUri,
            'fileType':fileType,
            'authorize':authorize,
            'localeIdsToAuthorize':localeIdsToAuthorize,
            'callbackUrl':callbackUrl,
        }
        self.addLibIdDirective(kw)
        self.processDirectives(kw, directives)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file')
        return self.uploadMultipart(url, kw)


    def downloadSourceFile(self, fileUri, **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/file
            details :  https://api-reference.smartling.com/#operation/downloadSourceFile
            as curl :  curl -H "Authorization: Bearer $smartlingToken" -G --data-urlencode "fileUri=$smartlingFileUri" "https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file"
        '''
        kw = {
            'fileUri':fileUri,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file', **kwargs)
        return self.command('GET', url, kw)


    def getFileTranslationStatusAllLocales(self, fileUri, **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/file/status
            details :  https://api-reference.smartling.com/#operation/getFileTranslationStatusAllLocales
        '''
        kw = {
            'fileUri':fileUri,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file/status', **kwargs)
        return self.command('GET', url, kw)


    def getFileTranslationStatusSingleLocale(self, localeId, fileUri, **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/locales/{localeId}/file/status
            details :  https://api-reference.smartling.com/#operation/getFileTranslationStatusSingleLocale
        '''
        kw = {
            'fileUri':fileUri,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/{localeId}/file/status', localeId=localeId, **kwargs)
        return self.command('GET', url, kw)


    def downloadTranslatedFileSingleLocale(self, localeId, fileUri, retrievalType='', includeOriginalStrings='', **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/locales/{localeId}/file
            details :  https://api-reference.smartling.com/#operation/downloadTranslatedFileSingleLocale
            as curl :  curl -H "Authorization: Bearer $smartlingToken" -o $smartlingLocaleId$smartlingFileUri -G --data-urlencode "fileUri=$smartlingFileUri" "https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/locales/$smartlingLocaleId/file"
        '''
        kw = {
            'fileUri':fileUri,
            'retrievalType':retrievalType,
            'includeOriginalStrings':includeOriginalStrings,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/{localeId}/file', localeId=localeId, **kwargs)
        return self.command('GET', url, kw)


    def downloadTranslatedFilesAllLocales(self, fileUri, retrievalType='', includeOriginalStrings='', zipFileName='', **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/locales/all/file/zip
            details :  https://api-reference.smartling.com/#operation/downloadTranslatedFilesAllLocales
            as curl :  curl -X GET -H "Authorization: Bearer $smartlingToken" 'https://api.smartling.com/files-api/v2/projects/{projectId}/locales/all/file/zip?fileUri=yourfile.json&retrievalType=published'
        '''
        kw = {
            'fileUri':fileUri,
            'retrievalType':retrievalType,
            'includeOriginalStrings':includeOriginalStrings,
            'zipFileName':zipFileName,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/all/file/zip', **kwargs)
        return self.command('GET', url, kw)


    def downloadMultipleTranslatedFiles(self, fileUris, localeIds, retrievalType='', includeOriginalStrings='', fileNameMode='', localeMode='', zipFileName='', **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/files/zip
            details :  https://api-reference.smartling.com/#operation/downloadMultipleTranslatedFiles
        '''
        kw = {
            'fileUris':fileUris,
            'localeIds':localeIds,
            'retrievalType':retrievalType,
            'includeOriginalStrings':includeOriginalStrings,
            'fileNameMode':fileNameMode,
            'localeMode':localeMode,
            'zipFileName':zipFileName,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/files/zip', **kwargs)
        return self.command('GET', url, kw)


    def getRecentlyUploadedSourceFilesList(self, uriMask='', fileTypes=[], lastUploadedAfter='', lastUploadedBefore='', orderBy='', limit=100, offset=0, **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/files/list
            details :  https://api-reference.smartling.com/#operation/getRecentlyUploadedSourceFilesList
            as curl :  curl -H "Authorization: Bearer $smartlingToken" "https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/files/list?fileTypes[]=json&uriMask=strings"
        '''
        kw = {
            'uriMask':uriMask,
            'fileTypes':fileTypes,
            'lastUploadedAfter':lastUploadedAfter,
            'lastUploadedBefore':lastUploadedBefore,
            'orderBy':orderBy,
            'limit':limit,
            'offset':offset,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/files/list', **kwargs)
        return self.command('GET', url, kw)


    def getFileTypesList(self, **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/file-types
            details :  https://api-reference.smartling.com/#operation/getFileTypesList
            as curl :  curl -H "Authorization: Bearer $smartlingToken" "https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file-types"
        '''
        kw = {
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file-types', **kwargs)
        return self.command('GET', url, kw)


    def renameUploadedSourceFile(self, fileUri, newFileUri, **kwargs):
        '''
            method  :  POST
            api url :  /files-api/v2/projects/{projectId}/file/rename
            details :  https://api-reference.smartling.com/#operation/renameUploadedSourceFile
            as curl :  curl -X POST -H "Authorization: Bearer $smartlingToken" -F "fileUri=filename.properties" -F "newFileUri=filename2.properties" 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file/rename'
        '''
        kw = {
            'fileUri':fileUri,
            'newFileUri':newFileUri,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file/rename', **kwargs)
        return self.command('POST', url, kw)


    def deleteUploadedSourceFile(self, fileUri, **kwargs):
        '''
            method  :  POST
            api url :  /files-api/v2/projects/{projectId}/file/delete
            details :  https://api-reference.smartling.com/#operation/deleteUploadedSourceFile
            as curl :  curl -X POST -H "Authorization: Bearer $smartlingToken" -F "fileUri=filename.properties" 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file/delete'
        '''
        kw = {
            'fileUri':fileUri,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file/delete', **kwargs)
        return self.command('POST', url, kw)


    def getTranslatedFileLastModifiedDateSingleLocale(self, localeId, fileUri, lastModifiedAfter='', **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/locales/{localeId}/file/last-modified
            details :  https://api-reference.smartling.com/#operation/getTranslatedFileLastModifiedDateSingleLocale
            as curl :  curl -X GET -H "Authorization: Bearer $smartlingToken" 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/locales/$smartlingLocaleId/file/last-modified?fileUri=filename.properties'
        '''
        kw = {
            'fileUri':fileUri,
            'lastModifiedAfter':lastModifiedAfter,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/{localeId}/file/last-modified', localeId=localeId, **kwargs)
        return self.command('GET', url, kw)


    def getTranslatedFileLastModifiedDateAllLocales(self, fileUri, lastModifiedAfter='', **kwargs):
        '''
            method  :  GET
            api url :  /files-api/v2/projects/{projectId}/file/last-modified
            details :  https://api-reference.smartling.com/#operation/getTranslatedFileLastModifiedDateAllLocales
            as curl :  curl -X GET -H "Authorization: Bearer $smartlingToken" 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/file/last-modified?fileUri=filename.properties'
        '''
        kw = {
            'fileUri':fileUri,
            'lastModifiedAfter':lastModifiedAfter,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/file/last-modified', **kwargs)
        return self.command('GET', url, kw)


    def importFileTranslations(self, localeId, file, fileUri, fileType, translationState, overwrite='', **kwargs):
        '''
            method  :  POST
            api url :  /files-api/v2/projects/{projectId}/locales/{localeId}/file/import
            details :  https://api-reference.smartling.com/#operation/importFileTranslations
            as curl :  curl -H "Authorization: Bearer $smartlingToken" -F "file=@filename.properties" -F "fileUri=filename.properties" -F "fileType=javaProperties" -F "translationState=PUBLISHED" 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/locales/$smartlingLocaleId/file/import'
        '''
        kw = {
            'file':self.processFile(file),
            'fileUri':fileUri,
            'fileType':fileType,
            'translationState':translationState,
            'overwrite':overwrite,
        }
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/{localeId}/file/import', localeId=localeId)
        return self.uploadMultipart(url, kw)


    def exportFileTranslations(self, localeId, file, fileUri, retrievalType='', includeOriginalStrings='', **kwargs):
        '''
            method  :  POST
            api url :  /files-api/v2/projects/{projectId}/locales/{localeId}/file/get-translations
            details :  https://api-reference.smartling.com/#operation/exportFileTranslations
            as curl :  curl -H "Authorization: Bearer $smartlingToken" -F "file=@filename.properties" -F 'fileUri=filename.properties' 'https://api.smartling.com/files-api/v2/projects/$smartlingProjectId/locales/$smartlingLocaleId/file/get-translations'
        '''
        kw = {
            'file':self.processFile(file),
            'fileUri':fileUri,
            'retrievalType':retrievalType,
            'includeOriginalStrings':includeOriginalStrings,
        }
        url = self.urlHelper.getUrl('/files-api/v2/projects/{projectId}/locales/{localeId}/file/get-translations', localeId=localeId)
        return self.uploadMultipart(url, kw)


    def getRecentlyPublishedFilesList(self, publishedAfter, fileUris=[], localeIds=[], offset=0, limit=0, **kwargs):
        '''
            method  :  GET
            api url :  /published-files-api/v2/projects/{projectId}/files/list/recently-published
            details :  https://api-reference.smartling.com/#operation/getRecentlyPublishedFilesList
            as curl :  curl -H "Authorization: Bearer $smartlingToken" 'https://api.smartling.com/published-files-api/v2/projects/$smartlingProjectId/files/list/recently-published?publishedAfter=2019-11-21T11:51:17Z&fileUris[]=files/example1.json&localeIds[]=fr-CA&limit=10&offset=100'
        '''
        kw = {
            'publishedAfter':publishedAfter,
            'fileUris':fileUris,
            'localeIds':localeIds,
            'offset':offset,
            'limit':limit,
        }
        kw.update(kwargs)
        url = self.urlHelper.getUrl('/published-files-api/v2/projects/{projectId}/files/list/recently-published', **kwargs)
        return self.command('GET', url, kw)

