on run {targetBuddyPhone, targetMessage, targetFile}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddyPhone of targetService

        set filenameLength to the length of targetFile
        if filenameLength > 0 then
            set attachment1 to (targetFile as POSIX file)
            send attachment1 to targetBuddy
        end if

        set messageLength to the length of targetMessage
        if messageLength > 0 then
            send targetMessage to targetBuddy
        end if
    end tell
end run